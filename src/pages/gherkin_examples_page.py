"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
from playwright.async_api import Page


class GherkinExamplesPage:

    def __init__(self, page: Page):
        self.elements_menu_option = page.get_by_role("heading", name="Elements")
        self.forms_menu_option = page.get_by_role("heading", name="Forms")
        self.text_box_option = page.get_by_text("Text Box")
        self.practice_form_option = page.get_by_text("Practice Form")
        self.full_name_input = page.locator("#userName")
        self.email_input = page.locator("#userEmail")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.submitted_data = page.locator('//*[@id="output"]/div')
        self.current_address_input = page.locator("#currentAddress")
        self.description_input = page.locator("#permanentAddress")

    async def click_elements_menu_option(self):
        await self.elements_menu_option.click()

    async def click_forms_menu_option(self):
        await self.forms_menu_option.click()

    async def click_text_box_option(self):
        await self.text_box_option.click()

    async def fill_full_name(self, name):
        await self.full_name_input.click()
        await self.full_name_input.fill(name)

    async def fill_email(self, email):
        await self.email_input.fill(email)

    async def click_submit_button(self):
        await self.submit_button.click()

    async def fill_current_address(self, address):
        await self.current_address_input.fill(address)

    async def fill_description(self, description):
        await self.description_input.fill(description)
