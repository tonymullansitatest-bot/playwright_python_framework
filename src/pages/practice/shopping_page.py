from playwright.async_api import expect
from sita_playwright_python_utils.playwright_util import *




class ShoppingPage:
    def __init__(self, page):
        self.page = page
        self.playwright_util = PlaywrightUtils(page)

        # Shopping page elements
        self.claw_hammer = page.get_by_text("Claw Hammer with Shock Reduction Grip")
        self.add_to_cart = page.get_by_test_id("add-to-cart")
        self.cart_quantity = page.get_by_test_id("cart-quantity")
        self.nav_cart = page.get_by_test_id("nav-cart")
        self.proceed_button = page.get_by_test_id("proceed-1")
        self.proceed_button_2 = page.get_by_test_id("proceed-2")
        self.proceed_button_3 = page.get_by_test_id("proceed-3")
        self.step_indicator = page.locator(".step-indicator")
        self.house_number = page.get_by_test_id("house_number")
        self.address = page.get_by_test_id("street")
        self.city = page.get_by_test_id("city")
        self.state = page.get_by_test_id("state")
        self.country = page.get_by_test_id("country")
        self.postcode = page.get_by_test_id("postal_code")
        self.finish = page.get_by_test_id("finish")
        self.payment_method = page.get_by_test_id("payment-method")
        self.monthly_installments = page.get_by_test_id("monthly_installments")
        self.help_block = page.locator(".help-block")


    # Method to purchase a product by its name
    async def purchase_product(self, product_name):
        
        target_product = self.page.get_by_text(product_name)
        await expect(target_product).to_be_visible()
        await target_product.click()
        await self.page.wait_for_load_state("networkidle")

        await expect(self.add_to_cart).to_be_visible()
        await expect(self.add_to_cart).to_be_enabled()
        await self.add_to_cart.click()
        await expect(self.cart_quantity).to_be_visible()
        await expect(self.cart_quantity).to_have_text("1")
        await self.nav_cart.click()
        await self.proceed_button.click()
        await self.proceed_button_2.click()
        step_2 = self.step_indicator.filter(has_text="2")
        await expect(step_2).to_have_css("background-color", "rgb(51, 153, 51)")
        await self.house_number.fill("123")
        await self.address.fill("123 Testing Way")
        await self.city.fill("Testville")
        await self.state.fill("Testonia")
        await self.country.select_option("Ireland")
        await self.postcode.fill("F93K1X1")
        await self.proceed_button_3.click()
        await expect(self.finish).to_be_disabled()
        await self.payment_method.select_option("Buy Now Pay Later")
        await self.monthly_installments.select_option("6 Monthly Installments")
        await expect(self.finish).to_be_enabled()
        await self.finish.click()
        await self.page.wait_for_load_state("networkidle")
        await expect(self.help_block).to_be_visible()
        await expect(self.help_block).to_have_text("Payment was successful")

