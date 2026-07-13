"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""

import re
from playwright.async_api import expect

from src.features.steps.parabank.parabank_steps import SESSION_STATE_FILE
from src.locators import parabank_locator
from sita_playwright_python_utils.playwright_util import *


class ParabankPage:
    def __init__(self, page):
        self.page = page
        self.playwright_util = PlaywrightUtils(page)

        # Top navigation / brand elements
        self.about_us_link = parabank_locator.about_us_link(page)
        self.parabank_img = parabank_locator.parabank_img(page)
        self.solutions_link = parabank_locator.solutions_link(page)
        self.services_link = parabank_locator.services_link(page)
        self.products_link = parabank_locator.products_link(page)
        self.locations_link = parabank_locator.locations_link(page)
        self.admin_page_link = parabank_locator.admin_page_link(page)
        self.register_link = parabank_locator.register_link(page)

        # Stable content on About page
        self.about_heading = parabank_locator.about_page_heading(page)
        self.overview_heading = parabank_locator.overview_page_heading(page)


        # Login form elements
        self.username_input = parabank_locator.username_input(page)
        self.password_input = parabank_locator.password_input(page)
        self.login_button = parabank_locator.login_button(page)

        self.account_id = parabank_locator.account_id(page)

    async def open_about_page(self):
        await self.page.goto("https://parabank.parasoft.com/parabank/about.htm")
        logger.log("Navigated to About Us page")

    async def click_parabank_image(self):
        await self.playwright_util.click_element(self.parabank_img)
        logger.log("Clicked Parabank image")

    async def click_about_us_link(self):
        await self.playwright_util.click_element(self.about_us_link)
        logger.log("Clicked About Us link")

    async def click_solutions_link(self):
        await self.playwright_util.click_element(self.solutions_link)
        logger.log("Clicked Solutions link")

    async def click_services_link(self):
        await self.playwright_util.click_element(self.services_link)
        logger.log("Clicked Services link")

    async def click_products_link(self):
        await self.playwright_util.click_element(self.products_link)
        logger.log("Clicked Products link")

    async def click_locations_link(self):
        await self.playwright_util.click_element(self.locations_link)
        logger.log("Clicked Locations link")

    async def click_admin_page_link(self):
        await self.playwright_util.click_element(self.admin_page_link)
        logger.log("Clicked Admin Page link")

    async def click_register_link(self):
        await self.playwright_util.click_element(self.register_link)
        logger.log("Clicked Register link")

    async def verify_about_page_loaded(self):
        await expect(self.about_heading).to_be_visible()
        await expect(self.page).to_have_url(re.compile(r".*/about.htm"))
        logger.log("About Us page loaded successfully")

    async def verify_services_page_loaded(self):
        await expect(self.page).to_have_url(re.compile(r".*/services.htm"))
        logger.log("Services page loaded successfully")

    async def verify_products_page_loaded(self):
        await expect(self.page).to_have_url(re.compile(r".*/products/"))
        logger.log("Products page loaded successfully") 

    async def verify_locations_page_loaded(self):
        await expect(self.page).to_have_url(re.compile(r".*/solutions/"))
        logger.log("Locations page loaded successfully")

    async def verify_admin_page_loaded(self):
        await expect(self.page).to_have_url(re.compile(r".*/admin.htm"))
        logger.log("Admin page loaded successfully")

    async def verify_overview_page_loaded(self):
        await expect(self.overview_heading).to_be_visible()
        await expect(self.page).to_have_url(re.compile(r".*/overview.htm"))
        logger.log("Overview page loaded successfully") 

    async def login(self, username, password):
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.login_button.click()
        logger.log(f"Attempted login with username: {username}")

    async def get_first_account_id(self):
        account_id = await self.account_id.text_content()
        logger.log(f"Retrieved account ID: {account_id}")
        return account_id.strip() if account_id else None
    
    async def visual_check_page(self, page_name):
        # Implement visual check logic here, e.g., using Playwright's screenshot comparison
        await self.page.wait_for_load_state("networkidle")  # Ensure the page is fully loaded
        screenshot_path = f"screenshots/{page_name}.png"
        await self.page.screenshot(path=screenshot_path)
        logger.log(f"Visual check for page '{page_name}' completed. Screenshot saved at {screenshot_path}") 

    async def delete_storage_state_file(self):
        if SESSION_STATE_FILE.exists():
            SESSION_STATE_FILE.unlink()
            logger.log(f"Deleted storage state file: {SESSION_STATE_FILE}")