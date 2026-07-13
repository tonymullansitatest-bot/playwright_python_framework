@test_api
Feature: Test Api

@api @121
Scenario: GET single resource api
    Given I send GET request to "/get"
    Then the status code should be 200
    And the response should contain keys ["url", "headers"]


@api
Scenario: GET resource with query parameters api
    Given I send GET request to "/get" with query params {"timestamp": "2026-02-13T12:00:00Z"}
    Then the status code should be 200
    And the response should contain keys ["args", "url"]


@api
Scenario: POST new user with static payload api
    Given I send "POST" request to "/post" with payload type "create_user"
    Then the status code should be 200
    And the response should contain keys ["json", "url"]

@api
Scenario: PUT update user with static payload
    Given I send "PUT" request to "/put" with payload type "update_user_full"
    #Given I send PUT request to "/put" with payload "user_update_full.json"
    Then the status code should be 200
    And the response should contain keys ["json", "url"]


@api
Scenario: DELETE resource
    Given I send "DELETE" request to "/delete"
    Then the status code should be 200
    And the response should contain keys ["url", "args"]

@api
Scenario: PATCH resource
    Given I send "PATCH" request to "/patch" with payload type "update_user_partial"
    Then the status code should be 200
    And the response should contain keys ["json", "url"]

@api
Scenario: POST new resource with dynamic payload
    Given I send "POST" request to "/post" with dynamic payload type "create_user_dynamic"
    Then the status code should be 200
    And the response should contain keys ["json", "url"]

@api
Scenario: Invalid GET request
    Given I send GET request to "/invalid_endpoint"
    Then the status code should be 404









