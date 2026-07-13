"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""


from sita_playwright_python_utils.playwright_util import *
from sita_playwright_python_utils.ExcelUtil import *
from utils.constants import EXCEL_DEMO_FILE
from utils.constants import EXCEL_DEFAULT_SHEET

class ExcelPage:

    def __init__(self, page: Page):
        self.page = page
        self.PlaywrightUtil = PlaywrightUtils(page)
        self.ExcelUtil = ExcelUtils()
        self.excel_demo_file_path = None


    async def have_excel_demo_file(self):
        self.excel_demo_file_path = self.ExcelUtil.verify_file_exists(EXCEL_DEMO_FILE)

        assert self.excel_demo_file_path and self.excel_demo_file_path.exists(), (
            f"Excel demo file exist"
            f"Received path: {self.excel_demo_file_path}"
        )

        logger.log(f"Using Excel file: {self.excel_demo_file_path}")
        return self.excel_demo_file_path

    """
        Reads a specific cell value from Excel and verifies it matches the expected value.
    """
    def get_and_verify_cell_value_from_excel(self, row: int, col: int, expected_value, sheet_name=None):
        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set.")

        row = int(row)
        col = int(col)
        value = self.ExcelUtil.get_cell_value(self.excel_demo_file_path, row, col, EXCEL_DEFAULT_SHEET)
        logger.log(f"Read cell value at ({row},{col}): {value}")

        if str(value) != str(expected_value):
            logger.log(f"Cell value mismatch at ({row},{col}): expected '{expected_value}', got '{value}'")
            raise AssertionError(
                f"Cell value at ({row},{col}) does not match. Expected '{expected_value}', got '{value}'")

        logger.log(f"Cell value at ({row},{col}) matches expected value: '{expected_value}'")
        return value

    """
        Retrieves the total number of rows in the Excel sheet and assert with expected_rows.
    """
    async def get_total_rows(self, expected_rows: int, sheet_name=None):
        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set.")

        total_rows = self.ExcelUtil.get_row_count(self.excel_demo_file_path, EXCEL_DEFAULT_SHEET)
        logger.log(f"Total rows: {total_rows}")
        assert total_rows == int(expected_rows), f"Expected {expected_rows} rows, but got {total_rows}"
        return total_rows

    """
        Retrieves the total number of columns in the Excel sheet.
    """
    async def get_total_columns(self, expected_cols: int, sheet_name=None):
        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set")

        total_cols = self.ExcelUtil.get_column_count(self.excel_demo_file_path, EXCEL_DEFAULT_SHEET)
        logger.log(f"Total columns: {total_cols}")
        assert total_cols == int(expected_cols), f"Expected {expected_cols} columns, but got {total_cols}"
        return total_cols

    """
        Write the specified value to the cell and verify it matches the expected value.
    """
    async def write_and_verify_cell_value(self, row: int, col: int, value: str, expected_value: str, sheet_name=None):
        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set")

        # Write the value using ExcelUtils method
        self.ExcelUtil.set_cell_value(self.excel_demo_file_path, row, col, value, EXCEL_DEFAULT_SHEET)

        # Verify the value
        actual_value = self.ExcelUtil.get_cell_value(self.excel_demo_file_path, row, col, EXCEL_DEFAULT_SHEET)
        logger.log(f"Verifying value at ({row},{col}): Expected '{expected_value}', Actual '{actual_value}'")

        # Assert actual value matches the expected value
        assert str(actual_value) == str(expected_value), f"Expected '{expected_value}', but got '{actual_value}'"
        logger.log(f"Successfully verified the cell value at ({row},{col}) is '{expected_value}'")

    """
        Reads a cell value from a specific sheet in Excel and verifies it matches the expected value.
    """
    async def get_cell_from_specific_sheet_two(self, sheet_name, row: int, col: int, expected_value):
        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set")

        if not sheet_name:
            raise ValueError("Sheet name must be provided")

        row = int(row)
        col = int(col)

        value = self.ExcelUtil.get_cell_value(
            self.excel_demo_file_path,
            row,
            col,
            sheet_name
        )

        logger.log(f"Reading from sheet '{sheet_name}' -> Cell ({row},{col}) = {value}")

        if str(value) != str(expected_value):
            logger.log(
                f"Mismatch in sheet '{sheet_name}' at ({row},{col}): "
                f"Expected '{expected_value}', got '{value}'"
            )
            raise AssertionError(
                f"Sheet '{sheet_name}' cell ({row},{col}) mismatch: "
                f"Expected '{expected_value}', got '{value}'"
            )

        logger.log(
            f"Verified sheet '{sheet_name}' cell ({row},{col}) matches expected value '{expected_value}'"
        )

        return value

    """
            Reads a row from Excel and validates all columns using a horizontal table from feature file.
    """
    async def read_and_validate_row_from_table_horizontal(self, row: int, sheet_name: str, table):

        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set")

        row_data = self.ExcelUtil.get_row_value(self.excel_demo_file_path, row, sheet_name)
        row_data = {k.strip(): v for k, v in row_data.items()}

        logger.log(f"Read row {row} from sheet '{sheet_name}': {row_data}")

        headings = [h.strip() for h in table.headings]
        expected_values = [v for v in table.rows[0]]

        for col_name, expected_value in zip(headings, expected_values):
            actual_value = row_data.get(col_name)

            if actual_value is None:
                raise AssertionError(f"Column '{col_name}' not found in Excel row {row}")

            if str(actual_value) != str(expected_value):
                logger.log(
                    f"Mismatch for '{col_name}' in row {row} of sheet '{sheet_name}': "
                    f"expected '{expected_value}', got '{actual_value}'"
                )
                raise AssertionError(
                    f"Row {row} value mismatch for '{col_name}' in sheet '{sheet_name}': "
                    f"expected '{expected_value}', got '{actual_value}'"
                )

            logger.log(f"Value for '{col_name}' matches expected: '{expected_value}'")

        return row_data

    """
            Reads a cell value from an invalid sheet and verifies the value is None.
    """
    async def read_cell_from_invalid_sheet_and_verify_null(
            self, row: int, col: int, sheet_name: str
    ):

        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set")

        logger.log(
            f"Trying to read cell ({row},{col}) from invalid sheet '{sheet_name}'"
        )

        try:
            value = self.ExcelUtil.get_cell_value(
                self.excel_demo_file_path,
                row,
                col,
                sheet_name
            )
        except KeyError:
            logger.log(f"Sheet '{sheet_name}' does not exist. Returning None.")
            value = None

        logger.log(f"Cell value read from invalid sheet: {value}")
        assert value is None, (
            f"Expected cell value to be None for invalid sheet '{sheet_name}', "
            f"but got '{value}'"
        )

        logger.log("Verified cell value is null as expected")
        return value

    """
            Reads the first row (headers) from the given sheet and verifies they match expected headers.
    """
    async def verify_column_headers(self, sheet_name: str, expected_headers: list):
        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set")

        actual_headers = []
        col_count = self.ExcelUtil.get_column_count(self.excel_demo_file_path, sheet_name)
        for col_no in range(1, col_count + 1):
            value = self.ExcelUtil.get_cell_value(self.excel_demo_file_path, 1, col_no, sheet_name)
            if value is not None:
                actual_headers.append(str(value).strip())

        logger.log(f"Actual headers from sheet '{sheet_name}': {actual_headers}")
        logger.log(f"Expected headers: {expected_headers}")

        assert actual_headers == expected_headers, (
            f"Column headers mismatch in sheet '{sheet_name}'. "
            f"Expected: {expected_headers}, Actual: {actual_headers}"
        )

        logger.log("Column headers verified successfully")

        """
            Verify that all values in a specific column match the expected values.
            Skips the header row and handles empty cells.
        """

    async def verify_column_values(self, col_index: int, expected_values: list, sheet_name=None):

        if not self.excel_demo_file_path:
            raise Exception("Excel demo file path not set")

        actual_values = self.ExcelUtil.get_column_values(self.excel_demo_file_path, col_index, sheet_name)

        # Convert all values to strings
        actual_values_str = [str(v) if v is not None else "" for v in actual_values]
        expected_values_str = [str(v) if v is not None else "" for v in expected_values]

        logger.log(f"Verifying column {col_index} values in sheet '{sheet_name}'")
        logger.log(f"Expected: {expected_values_str}")
        logger.log(f"Actual  : {actual_values_str}")

        assert actual_values_str == expected_values_str, (
            f"Mismatch in column {col_index} of sheet '{sheet_name}'. "
            f"Expected: {expected_values_str}, Got: {actual_values_str}"
        )

        logger.log(f"Column {col_index} values verified successfully")








