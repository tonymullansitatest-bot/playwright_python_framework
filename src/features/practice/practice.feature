@practice
Feature: Practice Test application

    Background:
        Given I log into practice test application

    Scenario: View practice overview
        Then I verify user page is loaded

    Scenario: I Purchase a product from the practice test application
        Then I Purchase a product from the practice test application

    Scenario: GET Purchased Details from api
        Given I send Practice GET request to "https://api.practicesoftwaretesting.com/products/search?q=thor%20hammer"
        Then the status code should be 200
        And the response should contain Thor Hammer with price 11.14

    Scenario: Validate the Authorization Token
        Then I confirm JWT Token is Valid
