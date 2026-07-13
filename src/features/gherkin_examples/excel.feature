@excel
Feature: Excel Utilities example

    @excel
    Scenario: 1 - Verify excel file exists
        Given I navigate to the my bag application
        When I verify the Excel demo file exist

    @excel
    Scenario: 2 - Get rows Count
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        Then total rows should be "5"

    @excel
    Scenario: 3 - Get columns count
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        Then total columns should be "3"

    @excel
    Scenario: 4 - Read a cell value from existing Excel file
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        When I read the value of cell row "2" and column "1" and verify value "John"

    @excel
    Scenario: 5 - Write and verify a cell value
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        When I write value "Doe" in row "3" column "1" and verify value "Doe"

    @excel
    Scenario: 6 - Read a cell value from second sheet
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        When I read the value from sheet "Sheet2" row "2" column "1" and verify value "Demo2"

    @excel
    Scenario: 7- Read column headers
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        When I read column headers of "Sheet1" and verify header value
            | Name | Age | City |

    @excel
    Scenario: 8 - Read cell value from invalid sheet
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        When I read cell at row "1" and column "1" from sheet "InvalidSheet" and verify null

    @excel
    Scenario: 9 - Read and validate a complete row from Excel
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        When I read and validate row "2" from sheet "Sheet1" with values
            | Name | Age | City |
            | John | 30  | London|

    @excel
    Scenario: 10 - Verify entire column values
        Given I navigate to the my bag application
        When I verify the Excel demo file exist
        When I verify column "2" values from sheet "Sheet1"
            |value|
            | 30 |
            | 25 |
            | 28 |
            | 22 |



