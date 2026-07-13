@parameters_example @regression
Feature: Examples for simple parameters, text parameters and table parameters

    @without_parameter @31001
    Scenario: PARAM1 - Scenario without parameter
        Given The user is on the demo page
        When The user navigates to the elements page
        Then The text box option is displayed

    @simple_parameter @214253 
    Scenario: PARAM2 - Scenario with simple parameter
        Given The user is on the demo page
        When The user navigates to the elements page
        And The user navigates to the text box page
        And Fill the full name with "John Doe"
        And Submits the form
        Then The name "John Doe" is displayed

    @text_parameter @214254
    Scenario: PARAM3 - Scenario with text parameter
        Given The user is on the demo page
        When The user navigates to the elements page
        And The user navigates to the text box page
        And Fill the description with
        """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
        enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat
        nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
        And Submits the form
        Then The description data are displayed

    @data_table_parameter  @214255
    Scenario: PARAM4 - Scenario with data table parameter
        Given The user is on the demo page
        When The user navigates to the elements page
        And The user navigates to the text box page
        And Fill the form with the following data
        | Full Name | Email Address    | Current Address |
        | John Doe  | johndoe@gmail.com| random address  |
        And Submits the form
        Then The data are displayed

