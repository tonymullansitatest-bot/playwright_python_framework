"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""


def about_us_link(page):
    return page.locator("#headerPanel").get_by_role("link", name="About Us")

def solutions_link(page):
    return page.locator("#headerPanel").get_by_role("link", name="Solutions")

def services_link(page):
    return page.locator("#headerPanel").get_by_role("link", name="Services")

def products_link(page):
    return page.locator("#headerPanel").get_by_role("link", name="Products")

def locations_link(page):
    return page.locator("#headerPanel").get_by_role("link", name="Locations")

def admin_page_link(page):
    return page.locator("#headerPanel").get_by_role("link", name="Admin Page")

def register_link(page):
    return page.locator("#bodyPanel").get_by_role("link", name="Register")

def parabank_img(page):
    return page.get_by_role("img", name="Parabank")

def about_page_heading(page):
    return page.get_by_role("heading", name="ParaSoft Demo Website")

def overview_page_heading(page):
    return page.get_by_role("heading", name="Accounts Overview")

def username_input(page):
    return page.locator("input[name=\"username\"]")

def password_input(page):
    return page.locator("input[name=\"password\"]")

def login_button(page):
    return page.get_by_role("button", name="Log In")

def account_id(page):
    return page.locator("#accountTable").locator("tbody tr").first.locator("td").first