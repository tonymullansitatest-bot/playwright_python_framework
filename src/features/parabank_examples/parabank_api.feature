@parabank_api
Feature: Test Initialize

@api
Scenario: POST Clean api
    Given I send Clean POST request to "cleanDB"
    Then The status code should be 204

@api
Scenario: POST Initialize api
    Given I send Initialize POST request to "initializeDB"
    Then The status code should be 204