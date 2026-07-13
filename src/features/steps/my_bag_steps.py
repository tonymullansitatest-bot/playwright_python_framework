"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
from behave import *
from behave.api.async_step import async_run_until_complete
#from src.locators.my_bag_locator import frame1_xpath


@given("I navigate to the my bag application")
@async_run_until_complete
async def step_impl(context):
    await context.page.goto(context.base_url)
    await context.pages.my_bag_page.click_accept_cookie_button()

@when("I click on the arrow down button")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.click_arrow_down_button()

@then("I check if the get started button is displayed")
@async_run_until_complete
async def step_impl(context):
    await  context.pages.my_bag_page.get_started_button_is_displayed()

@when('I select the "{airline}" airline')
@async_run_until_complete
async def step_impl(context, airline):
    await context.pages.my_bag_page.select_airline(airline)

@then('I verify airline "{airline}" is selected')
@async_run_until_complete()
async def step_impl(context, airline):
    await context.pages.my_bag_page.verify_airline_selected(airline)

@when('I print all dropdown option')
@async_run_until_complete()
async def step_impl(context):
    await context.pages.my_bag_page.get_dropdown_option()

@when("I click on get started button")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.click_main_get_started_button()

@then("I verify user is navigated to airline page and airline logo is displayed")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.verify_airline_page_and_logo()

@when("I click create a report widget")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.click_create_report_widget()

@when("I click manage an existing report report widget")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.click_manage_an_existing_report_widget()

@then("I click continue button")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.click_continue_button()

@when("I click add flight details")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.click_add_flight_details()


@then("I click single flight journey")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.click_single_flight_journey()

@then('I enter flight number "{number}"')
@async_run_until_complete
async def step_impl(context, number):
    await context.pages.my_bag_page.enter_flight_number(number)

@when('I verify text on my bag page')
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.verify_text_on_my_bag_page()

@then('I refresh the page')
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.refresh_demo_page()

@then('I navigate back to homepage')
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.navigate_back_to_home_page()

@then('I click on checkbox')
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.click_on_checkbox()

@then('I verify checkbox is selected')
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.verify_checkbox_is_selected()

@when("I clear enter flight number input field")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.clear_input_field()

@then("I verify input field enter flight number is empty")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.input_field_enter_flight_number_is_empty()

@then('I double click Flight departure date field')
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.double_click_Flight_departure_date_field()

@then('I verify calender is not displayed')
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.verify_calender_is_not_displayed()

@then('I press "{key}" Key')
@async_run_until_complete
async def step_impl(context, key):
    await context.pages.my_bag_page.press_keys(key)

@then('I verify url')
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.verify_current_url()

@then("I navigate to the alert page")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.navigate_to_alert_page()

@then("I navigate URL to hover over")
@async_run_until_complete
async def navigate_URL_to_hover(context):
    await context.pages.my_bag_page.navigate_URL_to_hover_over()

@then("I navigate to the airline page")
@async_run_until_complete
async def step_impl(context):
    await context.pages.my_bag_page.navigate_to_airline_page()

@when("I click simple alert button")
@async_run_until_complete
async def step_impl(context):
    context.alert_message = await context.pages.my_bag_page.click_simple_alert_button()

@then('I verify alert message is "{expected_message}"')
def step_impl(context, expected_message):
    assert context.alert_message == expected_message, f"Expected: {expected_message}, Got: {context.alert_message}"

@when("I click delayed alert button")
@async_run_until_complete
async def step_impl(context):
    context.alert_message = await context.pages.my_bag_page.click_delayed_alert_button()

@when("I click confirm alert accept button")
@async_run_until_complete
async def step_impl(context):
    context.alert_message = await context.pages.my_bag_page.click_confirm_ok()

@when("I click confirm alert dismiss button")
@async_run_until_complete
async def step_impl(context):
    context.alert_message = await context.pages.my_bag_page.click_confirm_cancel()

@when('I enter "{text}" in prompt alert')
@async_run_until_complete
async def step_impl(context, text):
    context.alert_message = await context.pages.my_bag_page.click_prompt_and_enter_text(text)

@when('I open a new tab')
@async_run_until_complete
async def step_when_open_new_tab(context):
    await context.pages.my_bag_page.open_new_browser_tab()

@then('I open another new tab')
@async_run_until_complete
async def step_when_open_new_tab(context):
    await context.pages.my_bag_page.open_another_new_tab()

@then('I switch to the first tab and verify the URL')
@async_run_until_complete
async def step_then_switch_to_first_tab_and_verify_url(context):
    await context.pages.my_bag_page.switch_to_first_tab()
    await context.pages.my_bag_page.verify_url_of_first_tab()

@then('I switch to the second tab and verify the URL')
@async_run_until_complete
async def step_then_switch_to_second_tab_and_verify_url(context):
    await context.pages.my_bag_page.switch_to_second_tab()
    await context.pages.my_bag_page.verify_url_of_second_tab()

@then('I verify that the first tab remains active')
@async_run_until_complete
async def step_then_verify_first_tab_still_open(context):
    await context.pages.my_bag_page.switch_to_first_tab()
    await context.pages.my_bag_page.verify_url_of_first_tab()

@then('I close the second tab')
@async_run_until_complete
async def step_when_close_second_tab(context):
    await context.pages.my_bag_page.close_current_tab()

@then('I switch to the newly opened tab')
@async_run_until_complete
async def step_then_switch_to_new_tab(context):
    await context.pages.my_bag_page.switch_to_new_tab()

@then('I verify the URL of the new tab')
@async_run_until_complete
async def step_then_verify_url_of_new_tab(context):
    await context.pages.my_bag_page.verify_url_of_new_tab()

@then('I verify widget count')
@async_run_until_complete
async def step_then_verify_url_of_new_tab(context):
    await context.pages.my_bag_page.verify_widget_count()

@then('I verify element is present')
@async_run_until_complete
async def step_then_verify_url_of_new_tab(context):
    await context.pages.my_bag_page.verify_element_is_present()

@then('I wait for url to load')
@async_run_until_complete
async def wait_for_url(context):
    await context.pages.my_bag_page.wait_for_url_to_load()

@then('I verify page title')
@async_run_until_complete
async def verify_title(context):
    await context.pages.my_bag_page.verify_page_title()

@then('I hover over edit icon')
@async_run_until_complete
async def hover_over_edit_icon(context):
    await context.pages.my_bag_page.hover_over_edit_icon()
