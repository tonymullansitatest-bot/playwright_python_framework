"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
from behave import given, when, then
from behave.api.async_step import async_run_until_complete

@when('I verify the Excel demo file exist')
@async_run_until_complete
async def step_have_excel_demo_file(context):
    await context.pages.my_excel_page.have_excel_demo_file()

@when('I read the value of cell row "{row}" and column "{col}" and verify value "{expected_value}"')
@async_run_until_complete
async def step_read_cell_value(context, row, col, expected_value):
    context.pages.my_excel_page.get_and_verify_cell_value_from_excel(row, col, expected_value)

@then('total rows should be "{expected_rows}"')
@async_run_until_complete
async def step_total_rows(context, expected_rows):
    await context.pages.my_excel_page.get_total_rows(expected_rows)

@then('total columns should be "{expected_cols}"')
@async_run_until_complete
async def step_total_columns(context, expected_cols):
    await context.pages.my_excel_page.get_total_columns(expected_cols)

@when('I write value "{value}" in row "{row}" column "{col}" and verify value "{expected_value}"')
@async_run_until_complete
async def step_write_and_verify_cell_value(context, value, row, col, expected_value):
    await context.pages.my_excel_page.write_and_verify_cell_value(int(row), int(col), value, expected_value)


@when('I read the value from sheet "{sheet_name}" row "{row}" column "{col}" and verify value "{expected_value}"')
@async_run_until_complete
async def step_read_cell_value_from_sheet(context, sheet_name, row, col, expected_value):
    await context.pages.my_excel_page.get_cell_from_specific_sheet_two(sheet_name=sheet_name, row=row, col=col, expected_value=expected_value)

@when('I read and validate row "{row}" from sheet "{sheet_name}" with values')
@async_run_until_complete
async def step_read_and_validate_row_from_table(context, row, sheet_name):
    await context.pages.my_excel_page.read_and_validate_row_from_table_horizontal(int(row),sheet_name,context.table)

@when('I read cell at row "{row}" and column "{col}" from sheet "{sheet_name}" and verify null')
@async_run_until_complete
async def step_read_cell_from_invalid_sheet(context, row, col, sheet_name):
    await context.pages.my_excel_page.read_cell_from_invalid_sheet_and_verify_null(int(row), int(col), sheet_name)

@when('I read column headers of "{sheet_name}" and verify header value')
@async_run_until_complete
async def step_read_column_headers(context, sheet_name):
    expected_headers = [h for h in context.table.headings]  # ['Name', 'Age', 'City']
    await context.pages.my_excel_page.verify_column_headers(sheet_name, expected_headers)

@when('I verify column "{col_index}" values from sheet "{sheet_name}"')
@async_run_until_complete
async def step_verify_column_values(context, col_index, sheet_name):
    expected_values = [row[0] for row in context.table]

    # Call page method to verify
    await context.pages.my_excel_page.verify_column_values(int(col_index), expected_values, sheet_name)







