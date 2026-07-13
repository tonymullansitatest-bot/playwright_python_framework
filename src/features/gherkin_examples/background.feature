@background_example @regression
Feature: Background example

    Background: Some requirements that are needed for all the scenarios
        Given The user is on the demo page

    @background_scenario_one @91003
    Scenario: Background scenario one
        When The user navigates to the elements page
        Then The text box option is displayed

    @background_scenario_two @96031
    Scenario: BACK02 - Background scenario two
        When The user navigates to the forms page
        Then The practice form option is displayed