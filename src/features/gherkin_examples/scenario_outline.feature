@scenario_outline_example @regression
Feature: Scenario outline example

    @outline_two_runs @214249
    Scenario Outline: OUT1 - Scenario outline which will run twice
        Given The user is on the demo page
        When The user navigates to the elements page
        And The user navigates to the text box page
        And Fill the full name with "<name>"
        And Submits the form
        Then The name "<name>" is displayed

    Examples:
        | name      |
        | John Doe  |
        | Anna Doe  |

    @outline_with_three_runs @214251
    Scenario Outline: OUT2 - Scenario outline with tag on the examples, which will run three times or just once if the tag is used
        Given The user is on the demo page
        When The user navigates to the elements page
        And The user navigates to the text box page
        And Fill the full name with "<name>"
        And Submits the form
        Then The name "<name>" is displayed

    @outline_with_two_runs
    Examples:
        | name      |
        | John Doe  |
        | Anna Doe  |

    @outline_with_one_run
    Examples:
        | name     |
        | Bill Doe |
