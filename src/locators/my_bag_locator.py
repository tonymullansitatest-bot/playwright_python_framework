"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""

accept_cookie_button_xpath = "//button[normalize-space()='Accept All Cookies']"
arrow_down_button_css = ".click-down-chevron"
landing_get_started_button_css = "#landing_get_started"
main_get_started_button_xpath = "//button[@aria-label='GET STARTED']"
airline_logo_css = "#logo_mobile"
select_airline_dropdown_css = "#ddl_select_airline"
language_button_css = "#lnk_select_language"
airline_logo_text_xpath = "//img[@id='logo_mobile']"
create_report_xpath = "//div[@aria-label='Create a report']"
manage_an_existing_report_widget_xpath = "//div[@aria-label='manage an existing report']"
homepage_header_text_xpath = "//div[@class='landing-title container']//h1[@id='menu_head']"
remember_details_checkbox_xpath = "//input[@id='chk_RememberMe']/..//label"
flight_departure_date_box_xpath = "//button//img[@aria-label='Open Calendar1']"
calender_next_month_arrow_xpath = "//button[@aria-label='Next month']"
click_button_to_see_alert_xpath = "//button[@id='alertButton']"
delayed_alert_button_xpath = "//button[@id='timerAlertButton']"
confirm_alert_button_xpath = "//button[@id='confirmButton']"
prompt_box_alert_button_xpath = "//button[@id='promtButton']"
# frame1_xpath = "//iframe[@id='frame1']"
# frame2_xpath = "//iframe[@id='frame2']"
text_heading_one_xpath = " //h1[@id='sampleHeading']"
widget_xpath = "//div[@class='logo main_menu']"
widget_1_xpath = "(//div[@class='logo main_menu'])[1]"
hover_over_button_xpath = "//div[@id='myDropdown']"
hover_over_text_xpath = "//a[@id='dropOption1']"

def continue_button(page):
    return page.get_by_role("button", name="CONTINUE")

def add_flight_detail(page):
    return page.get_by_role("button", name="Add flight details")

def single_flight_journey(page):
    return page.get_by_role("button", name="Single leg flight Single")

def flight_number_textbox(page):
   return page.get_by_role("textbox", name="Flight number1")



