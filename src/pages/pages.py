"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
from src.pages.excel_page import ExcelPage
from src.pages.gherkin_examples_page import GherkinExamplesPage
from src.pages.my_bag_page import MyBaGPage
from src.pages.parabank_page import ParabankPage
from src.pages.parabank_register_page import ParabankRegisterPage
from src.pages.practice.login_page import LoginPage
from src.pages.practice.shopping_page import ShoppingPage


class Pages:

    def __init__(self, context):
        self.gherkin_examples_page = GherkinExamplesPage(context.page)
        self.my_bag_page = MyBaGPage(context.page)
        self.my_excel_page = ExcelPage(context.page)
        self.parabank_page = ParabankPage(context.page)
        self.parabank_register_page = ParabankRegisterPage(context.page)
        self.login_page = LoginPage(context.page)
        self.shopping_page = ShoppingPage(context.page)