"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
from playwright.async_api import Page
from sita_playwright_python_utils.playwright_util import *


class ParabankRegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_util = PlaywrightUtils(page)

        self.first_name_input = page.locator("#customer\\.firstName")
        self.last_name_input = page.locator("#customer\\.lastName")
        self.address_input = page.locator("#customer\\.address\\.street")
        self.city_input = page.locator("#customer\\.address\\.city")
        self.state_input = page.locator("#customer\\.address\\.state")
        self.zip_code_input = page.locator("#customer\\.address\\.zipCode")
        self.phone_input = page.locator("#customer\\.phoneNumber")
        self.ssn_input = page.locator("#customer\\.ssn")
        self.username_input = page.locator("#customer\\.username")
        self.password_input = page.locator("#customer\\.password")
        self.confirm_password_input = page.locator("#repeatedPassword")
        self.register_button = page.locator("#customerForm").get_by_role("button", name="Register")

    async def fill_registration_form(self, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password):
        await self.first_name_input.fill(first_name)
        await self.last_name_input.fill(last_name)
        await self.address_input.fill(address)
        await self.city_input.fill(city)
        await self.state_input.fill(state)
        await self.zip_code_input.fill(zip_code)
        await self.phone_input.fill(phone)
        await self.ssn_input.fill(ssn)
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.confirm_password_input.fill(password)
        await self.register_button.click()
        logger.log("Filled registration form and submitted")

