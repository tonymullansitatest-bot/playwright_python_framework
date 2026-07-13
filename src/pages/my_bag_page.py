"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""

from src.locators import my_bag_locator

from sita_playwright_python_utils.playwright_util import *
import utils.constants as constants


class MyBaGPage:

    def __init__(self, page: Page):
        self.page = page
        self.PlaywrightUtil = PlaywrightUtils(page)
        self.accept_cookie_button = page.locator(my_bag_locator.accept_cookie_button_xpath)
        self.arrow_down_button = page.locator(my_bag_locator.arrow_down_button_css)
        self.landing_get_started_button = page.locator(my_bag_locator.landing_get_started_button_css)
        self.main_get_started_button = page.locator(my_bag_locator.main_get_started_button_xpath)
        self.airline_logo = page.locator(my_bag_locator.airline_logo_css)
        self.select_airline_dropdown = page.locator(my_bag_locator.select_airline_dropdown_css)
        self.language_button = page.locator(my_bag_locator.language_button_css)
        self.airline_logo_text = page.locator(my_bag_locator.airline_logo_text_xpath)
        self.create_report_widget = page.locator(my_bag_locator.create_report_xpath)
        self.manage_an_existing_report = page.locator(my_bag_locator.manage_an_existing_report_widget_xpath)
        self.continue_button = my_bag_locator.continue_button(page)
        self.add_flight_details = my_bag_locator.add_flight_detail(page)
        self.single_flight_journey_button = my_bag_locator.single_flight_journey(page)
        self.flight_number_textbox_field = my_bag_locator.flight_number_textbox(page)
        self.homepage_header_text = page.locator(my_bag_locator.homepage_header_text_xpath)
        self.remember_details_checkbox = page.locator(my_bag_locator.remember_details_checkbox_xpath)
        self.flight_departure_date_box = page.locator(my_bag_locator.flight_departure_date_box_xpath)
        self.calender_next_month_arrow = page.locator(my_bag_locator.calender_next_month_arrow_xpath)
        self.click_button_to_see_alert = page.locator(my_bag_locator.click_button_to_see_alert_xpath)
        self.delayed_alert_button = page.locator(my_bag_locator.delayed_alert_button_xpath)
        self.confirm_alert_button = page.locator(my_bag_locator.confirm_alert_button_xpath)
        self.prompt_box_alert_button = page.locator(my_bag_locator.prompt_box_alert_button_xpath)
        # self.frame1 =  page.locator(my_bag_locator.frame1_xpath)
        # self.frame2 = page.locator(my_bag_locator.frame2_xpath)
        self.text_heading_one = page.locator(my_bag_locator.text_heading_one_xpath)
        self.widget = page.locator(my_bag_locator.widget_xpath)
        self.widget_1 = page.locator(my_bag_locator.widget_1_xpath)
        self.hover_over_button = page.locator(my_bag_locator.hover_over_button_xpath)
        self.hover_over_text = page.locator(my_bag_locator.hover_over_text_xpath)

    #Method to click accept cookie button
    async def click_accept_cookie_button(self):
        await self.PlaywrightUtil.click_element(self.accept_cookie_button)
        logger.log("clicked on Accept Cookies Button")

    #Method to click arrow down button
    async def click_arrow_down_button(self):
        await self.PlaywrightUtil.click_element(self.arrow_down_button)
        logger.log("clicked on Arrow Down Button")

    #This method is used to verify button is displayed
    async  def get_started_button_is_displayed(self):
        await self.PlaywrightUtil.assert_element_is_visible(self.landing_get_started_button)
        logger.log("get started button is displayed")

    async def click_main_get_started_button(self):
        await self.PlaywrightUtil.click_element(self.main_get_started_button)
        logger.log("clicked on Get started Button")

    # This method is used to select airline from dropdown
    async def select_airline(self, airline):
        await self.PlaywrightUtil.select_option_by_value_from_dropdown(self.select_airline_dropdown, airline)
        logger.log("Selected dropdown option: " +airline)
        await asyncio.sleep(2)

    #Method to verify dropdown value present in dropdown
    async def verify_airline_selected(self, airline):
        selected_value =  await self.PlaywrightUtil.get_selected_option_from_dropdown(self.select_airline_dropdown)
        assert selected_value == airline, f"Expected value '{airline}', but got '{selected_value}'"
        logger.log(f"Verified selected airline: expected: {airline} Actual: '{selected_value}'")

    async def get_dropdown_option(self):
        options = await self.PlaywrightUtil.get_all_dropdown_options(self.select_airline_dropdown)
        logger.log(f"dropdown list is'{options}'")

    #Method to verify airline page and logo
    async def verify_airline_page_and_logo(self):
        expected_url = constants.AIRLINE_URL
        await self.page.wait_for_url(expected_url)
        logger.log(f"Navigated to expected airline URL: {expected_url}")

        await self.PlaywrightUtil.assert_element_is_visible(self.airline_logo)
        logger.log("verified airline logo is displayed")

        #get attribute value
        fetch_value = await self.PlaywrightUtil.get_attribute_value(self.airline_logo_text,"alt")
        expected_vale = constants.AIRLINE_Name
        assert fetch_value == expected_vale, f"Expected value of logo text '{expected_vale}', but got '{fetch_value}'"

    async def click_create_report_widget(self):
        await self.PlaywrightUtil.click_element(self.create_report_widget)
        logger.log("clicked on Create report widget")
        await asyncio.sleep(2)

    async def click_manage_an_existing_report_widget(self):
        await self.PlaywrightUtil.click_element(self.manage_an_existing_report)
        logger.log("clicked on manage an existing report widget")
        await asyncio.sleep(1)

    async def click_continue_button(self):
        await self.PlaywrightUtil.click_element(self.continue_button)
        logger.log("clicked on continue button")

    async def click_add_flight_details(self):
        await self.PlaywrightUtil.click_element(self.add_flight_details)
        logger.log("clicked on add flight details")

    async def click_single_flight_journey(self):
        await self.PlaywrightUtil.click_element(self.single_flight_journey_button)
        logger.log("clicked on single flight journey")

    async def enter_flight_number(self, number):
        await self.PlaywrightUtil.type_values_in_a_textbox(self.flight_number_textbox_field, number)
        logger.log("Entered flight number: " + number)
        await asyncio.sleep(2)

    async def verify_text_on_my_bag_page(self):
        actual_text  = await self.PlaywrightUtil.get_text(self.homepage_header_text)
        expected_text = constants.HOMEPAGE_HEADER
        logger.log(f"Verifying homepage header text. Expected: '{expected_text}' | Actual: '{actual_text}'")
        assert actual_text == expected_text, (
            f"Header text mismatch. Expected: '{expected_text}', but found: '{actual_text}'"
        )
        logger.log("Header text verified successfully.")

    async def refresh_demo_page(self):
        await self.PlaywrightUtil.refresh_page()

    async def navigate_back_to_home_page(self):
        await self.PlaywrightUtil.navigate_back()

    async def click_on_checkbox(self):
        await self.PlaywrightUtil.click_element(self.remember_details_checkbox)

    async def verify_checkbox_is_selected(self):
        is_checked = await self.PlaywrightUtil.is_checked(self.remember_details_checkbox)
        assert is_checked, "The 'Remember Details' checkbox is not selected."
        logger.log("'Remember Details' checkbox is verified as selected.")

    async def clear_input_field(self):
        await  self.PlaywrightUtil.clear_element(self.flight_number_textbox_field)

    async def input_field_enter_flight_number_is_empty(self):
        actual_value = await self.PlaywrightUtil.get_text(self.flight_number_textbox_field)
        assert actual_value == "", f"Expected ' empty', got '{actual_value}'"

    async def double_click_Flight_departure_date_field(self):
        await self.PlaywrightUtil.double_click_element(self.flight_departure_date_box)
        await asyncio.sleep(2)
        logger.log("Double Click on Flight Departure Date")

    async def verify_calender_is_not_displayed(self):
        is_visible = await self.PlaywrightUtil.is_element_visible(self.calender_next_month_arrow)
        assert not is_visible, f"Expected the calendar to not be displayed, but it is visible."

    async def press_keys(self, keys):
        await self.PlaywrightUtil.press_key(keys)

    async def verify_current_url(self):
        expected_url = constants.ALERT_URL
        current_url = await self.PlaywrightUtil.get_current_url()
        assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
        logger.log(f"Verified that the current URL matches the expected URL: {expected_url}")

    async def navigate_to_alert_page(self):
        alert_url = constants.ALERT_URL
        await self.PlaywrightUtil.navigate_to_url(alert_url)
        logger.log(f"Navigated to Url: {alert_url}")

    async def navigate_URL_to_hover_over(self):
        alert_url = constants.HOVER_OVER_URL
        await self.PlaywrightUtil.navigate_to_url(alert_url)
        logger.log(f"Navigated to Url: {alert_url}")

    async def navigate_to_airline_page(self):
        alert_url = constants.AIRLINE_URL
        await self.PlaywrightUtil.navigate_to_url(alert_url)
        logger.log(f"Navigated to Url: {alert_url}")

    async def click_simple_alert_button(self):
        return await self.PlaywrightUtil.handle_alert(
            trigger_action=lambda: self.PlaywrightUtil.click_element(self.click_button_to_see_alert),
            action="accept"
        )

    async def click_delayed_alert_button(self):
        return await self.PlaywrightUtil.handle_alert(
            trigger_action=lambda: self.PlaywrightUtil.click_element(self.delayed_alert_button),
            action="accept"
        )

    async def click_confirm_ok(self):
        return await self.PlaywrightUtil.handle_alert(
            trigger_action=lambda: self.PlaywrightUtil.click_element(self.confirm_alert_button),
            action="accept"
        )

    async def click_confirm_cancel(self):
        return await self.PlaywrightUtil.handle_alert(
            trigger_action=lambda: self.PlaywrightUtil.click_element(self.confirm_alert_button),
            action="dismiss"
        )

    async def click_prompt_and_enter_text(self, text):
        return await self.PlaywrightUtil.handle_alert(
            trigger_action=lambda: self.PlaywrightUtil.click_element(self.prompt_box_alert_button),
            action="accept",
            prompt_text=text
        )

    async def open_new_browser_tab(self):
        await self.PlaywrightUtil.open_new_tab()

    async def open_another_new_tab(self):
        await self.PlaywrightUtil.open_new_tab()

    async def switch_to_first_tab(self):
        await self.PlaywrightUtil.switch_window(0)
        logger.log("Switched to the first tab.")

    async def switch_to_second_tab(self):
        await self.PlaywrightUtil.switch_window(1)
        logger.log("Switched to the second tab.")

    async def verify_url_of_first_tab(self):
        expected_url = constants.HOMEPAGE_URL
        current_url = await self.PlaywrightUtil.get_current_url()
        logger.log(f"Current URL of first tab: {current_url}")

        if current_url == expected_url:
            logger.log(f"Verified: First tab's URL is correct: {current_url}")
        else:
            raise Exception(f"URL mismatch: Expected {expected_url}, but got {current_url}")

    async def verify_url_of_second_tab(self):
        expected_url = constants.AIRLINE_URL
        current_url = await self.PlaywrightUtil.get_current_url()
        logger.log(f"Current URL of first tab: {current_url}")

        if current_url == expected_url:
            logger.log(f"Verified: Second tab's URL is correct: {current_url}")
        else:
            raise Exception(f"URL mismatch: Expected {expected_url}, but got {current_url}")

    async def close_current_tab(self):
        await self.PlaywrightUtil.close_tab()
        logger.log("Closed the current tab.")

    async def switch_to_new_tab(self):
        try:
            all_pages = self.PlaywrightUtil.page.context.pages
            new_tab_index = len(all_pages) - 1
            await self.PlaywrightUtil.switch_window(new_tab_index)
            logger.log("Switched to the newly opened tab.")
        except Exception as e:
            logger.log(f"Failed to switch to the new tab: {str(e)}")
            raise Exception(f"Failed to switch to the new tab. Reason: {str(e)}")

    async def verify_url_of_new_tab(self):
        expected_url =constants.ALERT_URL
        try:
            current_url = self.PlaywrightUtil.page.url
            logger.log(f"Current URL is: {current_url}")
            if current_url == expected_url:
                logger.log(f"Verified: The new tab's URL is as expected: {current_url}")
            else:
                raise Exception(f"URL mismatch: Expected {expected_url}, but got {current_url}")
        except Exception as e:
            logger.log(f"Failed to verify new tab URL: {str(e)}")
            raise Exception(f"Failed to verify new tab URL. Reason: {str(e)}")

    async def verify_first_tab_url(self):
        await self.navigate_to_alert_page()

    async def verify_widget_count(self):
        await asyncio.sleep(2)
        count = await self.PlaywrightUtil.get_elements_count(self.widget)

        if count == 3:
            logger.log("Correct number of products displayed.")
        else:
            raise Exception("Product count mismatch.")

    async def verify_element_is_present(self):
        await asyncio.sleep(2)
        is_present = await self.PlaywrightUtil.is_element_exists(self.widget_1)
        assert is_present, "Element is not present on the page"

    async def wait_for_url_to_load(self):
        expected_url = constants.AIRLINE_URL
        await self.PlaywrightUtil.wait_for_url(expected_url)
        logger.log("user is navigated to url")

    async def verify_page_title(self):
        expected_title = constants.PAGE_TITLE
        actual_title = await self.PlaywrightUtil.get_title()
        assert actual_title == expected_title, \
            f"Page title mismatch. Expected: '{expected_title}', Got: '{actual_title}'"
        logger.log(f"Page title verified. {actual_title}")

    async def hover_over_edit_icon(self):
        await self.PlaywrightUtil.hover(self.hover_over_button)
        logger.log("Hovering over the edit icon.")
        actual_text = await self.PlaywrightUtil.get_text(self.hover_over_text)
        logger.log(f"Hovering over text is {actual_text}")

