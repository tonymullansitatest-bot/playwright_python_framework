@parabank_register
Feature: Parabank application register user

    @parabank_register
    Scenario: - Register User
        Given I navigate to the parabank application
        When Fill the form with data from register user file
        Then I delete the storage state file