@parabank
Feature: Parabank application

    Background:
        Given I navigate to the parabank application
        And I log into parabank application
    
    Scenario: View accounts overview
        Then I verify overview page is loaded
        And I store the account id
        And I visual check the page "account overview"

    Scenario: Click on the Header Panel Links
        Given I navigate to the parabank application
        When I click on about us link
        Then I verify about us page is loaded
        When I click on services link
        Then I verify services page is loaded
        When I click on products link
        Then I verify products page is loaded
        When I click on locations link
        Then I verify locations page is loaded
        When I click on admin page link
        Then I verify admin page is loaded

    Scenario: GET Account api
    Given I send Account GET request to "accounts/99999"
    Then the status code should be 200
    And the response should contain xml tag "id" with value "24666"
    And the response should contain xml tag "type" with value "CHECKING"

    Scenario: Post Funds into account
    Given I deposit the following Funds POST request to "deposit":
        | account      | amount |
        | CHECKING     | 100   |
        | CHECKING     | 290   |
        | CHECKING     | 555   |
    Then the status code should be 200

    Scenario: Get Account balance and Customer id
    Given I get Account balance and customer id GET request to "accounts/99999"
    Then I validate balance is updated and customer id is present in response "1460.50"

    Scenario: GET Account Transactions api
    Given I send Transactions GET request to "accounts/99999/transactions"
    Then the status code should be 200


