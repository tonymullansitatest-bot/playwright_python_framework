from venv import logger

from playwright.async_api import expect

from sita_playwright_python_utils.playwright_util import *

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.playwright_util = PlaywrightUtils(page)

        # Login form elements
        self.username_input = page.locator('[data-test="email"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-submit"]')
        self.nav_menu = page.locator('[data-test="nav-menu"]')

    async def go_to_login_page(self):
        await self.page.goto("https://practicesoftwaretesting.com" + "/auth/login")
        logger.log("Navigated to Login page")
        

    async def login(self, email, password):
        await self.username_input.fill(email)
        await self.password_input.fill(password)
        await self.login_button.click()
        logger.log(f"Logged in with email: {email}")

    async def verify_login_successful(self,name="Jane Doe"):
        # Wait for the page to load and check for an element that indicates a successful login
        await expect(self.page).to_have_url("https://practicesoftwaretesting.com/account")
        await expect(self.nav_menu).to_contain_text(name)
        logger.log("Login successful, navigated to account page")