@my_bag
Feature: My bag application

    @Bag01 @click_element @121
    Scenario: 01 - Click on the arrow down button
        Given I navigate to the my bag application
        When I click on the arrow down button

    @Bag01 @type_values_in_a_textbox
    Scenario Outline: 02 - enter flight number
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        Then I verify user is navigated to airline page and airline logo is displayed
        When I click create a report widget
        Then I click continue button
        When I click add flight details
        Then I click single flight journey
        Then I enter flight number "<flightNumber>"

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @get_text
    Scenario: 03 - Verify text on my bag page
        Given I navigate to the my bag application
        When I verify text on my bag page

    @Bag01 @assert_element_is_visible
    Scenario: 04 - Get started button displayed on the home page after scrolling
        Given I navigate to the my bag application
        When I click on the arrow down button
        Then I check if the get started button is displayed

    @Bag01 @get_attribute_value
    Scenario Outline: 05 - Navigated to airline page and airline logo is displayed
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        Then I verify user is navigated to airline page and airline logo is displayed

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @select_option_by_value_from_dropdown
    Scenario Outline: 06 - selection of airline from dropdown
        Given I navigate to the my bag application
        When I select the "<airline>" airline

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @get_selected_option_from_dropdown
    Scenario Outline: 07 - verify airline selected from dropdown
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @is_checkbox_checked
    Scenario Outline: 08 - Verify checkbox is selected
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        When I click manage an existing report report widget
        Then I click on checkbox
        Then I verify checkbox is selected

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @refresh_page
    Scenario Outline: 09 - Refresh airline page
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        Then I refresh the page

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @navigate_back
    Scenario Outline: 10 - Navigate back to homepage
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        Then I navigate back to homepage

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @clear_action
    Scenario Outline: 11 - clear input field
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        Then I verify user is navigated to airline page and airline logo is displayed
        When I click create a report widget
        Then I click continue button
        When I click add flight details
        Then I click single flight journey
        Then I enter flight number "<flightNumber>"
        #Then I verify field is populated with text "<flightNumber>"
        When I clear enter flight number input field
        Then I verify input field enter flight number is empty

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @double_click_element @is_element_visible
    Scenario Outline: 12 - perform double click action
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        Then I verify user is navigated to airline page and airline logo is displayed
        When I click create a report widget
        Then I click continue button
        When I click add flight details
        Then I click single flight journey
        Then I enter flight number "<flightNumber>"
        And I double click Flight departure date field
        And I verify calender is not displayed

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |


    @Bag01 @press_key
    Scenario Outline: 13 - press keys
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        Then I verify user is navigated to airline page and airline logo is displayed
        When I click create a report widget
        Then I click continue button
        When I click add flight details
        Then I click single flight journey
        Then I enter flight number "<flightNumber>"
        Then I press "ArrowLeft" Key
        Then I press "ArrowRight" Key
        Then I press "CapsLock" Key
        Then I enter flight number "jjn"
        Then I press "ArrowUp" Key
        Then I press "Tab" Key

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @navigate_to_url
    Scenario: 14 - Navigate to url
        Given I navigate to the my bag application
        Then I navigate to the alert page

    @Bag01 @get_current_url
    Scenario: 15 - verify current URL
        Given I navigate to the my bag application
        Then I navigate to the alert page
        Then I verify url

    @Bag01 @simple_alert_handle
    Scenario: 16 - Simple Alert
        Given I navigate to the my bag application
        Then I navigate to the alert page
        When I click simple alert button
        Then I verify alert message is "You clicked a button"

    @Bag01 @delayed_alert_handle
    Scenario: 17 - Delayed Alert
        Given I navigate to the my bag application
        Then I navigate to the alert page
        When I click delayed alert button
        Then I verify alert message is "This alert appeared after 5 seconds"

    @Bag01 @confirm_alert
    Scenario: 18 - Confirm Alert - Accept
        Given I navigate to the my bag application
        Then I navigate to the alert page
        When I click confirm alert accept button
        Then I verify alert message is "Do you confirm action?"

    @Bag01 @dismiss_alert
    Scenario: 19 - Confirm Alert - Dismiss
        Given I navigate to the my bag application
        Then I navigate to the alert page
        When I click confirm alert dismiss button
        Then I verify alert message is "Do you confirm action?"

    @Bag01 @prompt_alert
    Scenario: 20 - Prompt Alert
        Given I navigate to the my bag application
        Then I navigate to the alert page
        When I enter "HelloSita" in prompt alert

    @Bag01 @open_new_tab @switch_to_two_tabs
  Scenario: 21 - Open two tabs, switch between them, and verify their URLs
    Given I navigate to the my bag application
    When I open a new tab
    Then I navigate to the airline page
    Then I open another new tab
    Then I navigate to the airline page
    Then I switch to the first tab and verify the URL
    And I switch to the second tab and verify the URL
    And I close the second tab
    Then I verify that the first tab remains active

    @Bag01 @open_new_tab @switch_to_new_tab
    Scenario: 22 - Open a new tab and verify the URL of the newly opened tab
    Given I navigate to the my bag application
    When I open a new tab
    Then I switch to the newly opened tab
    Then I navigate to the alert page
    Then I verify the URL of the new tab

    @Bag01 @is_element_exists
    Scenario Outline: 23 - check element present
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        Then I verify element is present

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @get_elements_count
    Scenario Outline: 24 - Retrieve the number of matched elements count
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I click on get started button
        Then I verify widget count

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @get_all_dropdown_options
    Scenario Outline: 25 - get all options
        Given I navigate to the my bag application
        When I select the "<airline>" airline
        Then I verify airline "<airline>" is selected
        When I print all dropdown option

            Examples:
                |airline  |flightNumber|
                | UX      |XYZ007      |

    @Bag01 @wait_for_url
    Scenario: 26 - wait for url
        Given I navigate to the my bag application
        Then I navigate to the airline page
        Then I wait for url to load

    @Bag01 @get_title
    Scenario: 27 - get title
        Given I navigate to the my bag application
        Then I verify page title

    @Bag01 @hover
    Scenario: 28 - hover over element
        Given I navigate to the my bag application
        Then I navigate URL to hover over
        Then I hover over edit icon








