"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
from behave import *
from behave.api.async_step import async_run_until_complete
import json
from utils.constants import TEST_DATA_DIR
from pathlib import Path

SESSION_STATE_FILE = Path("debug") / "parabank_storage_state.json"


@given("I navigate to the parabank application")
@async_run_until_complete
async def step_impl(context):
    await context.page.goto(context.base_url)
    await context.pages.parabank_page.click_parabank_image()

@when("I click on about us link")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.click_about_us_link()

@then("I verify about us page is loaded")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.verify_about_page_loaded()

@when("I click on solutions link")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.click_solutions_link()

@then("I verify solutions page is loaded")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.verify_solutions_page_loaded()

@when("I click on services link")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.click_services_link()

@then("I verify services page is loaded")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.verify_services_page_loaded()

@when("I click on products link")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.click_products_link()  

@then("I verify products page is loaded")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.verify_products_page_loaded()
    await context.page.go_back()  # Navigate back to the main page after clicking products link   

@when("I click on locations link")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.click_locations_link()

@then("I verify locations page is loaded")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.verify_locations_page_loaded()
    await context.page.go_back()  # Navigate back to the main page after clicking locations link

@when("I click on admin page link")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.click_admin_page_link()

@then("I verify admin page is loaded")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.verify_admin_page_loaded()


@when("Fill the form with data from register user file")
@async_run_until_complete
async def step_fill_form_from_json(context):

    file_path = TEST_DATA_DIR / "parabank_user_register.json"
    with open(file_path) as f:
        data = json.load(f)
    await context.pages.parabank_page.click_register_link()
    await context.pages.parabank_register_page.fill_registration_form(
        first_name=data["first_name"],
        last_name=data["last_name"],
        address=data["address"],
        city=data["city"],
        state=data["state"],
        zip_code=data["zip_code"],
        phone=data["phone"],
        ssn=data["ssn"],
        username=data["username"],
        password=data["password"]
    )

@given("I log into parabank application")
@when("I log into parabank application")
@async_run_until_complete
async def step_login_from_json(context):
    # Reuse the saved authenticated state when available to avoid logging in for every scenario.
    if SESSION_STATE_FILE.exists():
        with open(SESSION_STATE_FILE, encoding="utf-8") as f:
            state = json.load(f)

        cookies = state.get("cookies", [])
        if cookies:
            await context.page.context.add_cookies(cookies)

        #await context.page.goto(f"{context.base_url.rstrip('/')}/overview.htm")
        await context.page.goto(f"{context.base_url}")
        return

    file_path = TEST_DATA_DIR / "parabank_user_register.json"
    with open(file_path) as f:
        data = json.load(f)
    await context.pages.parabank_page.login(
        username=data["username"],
        password=data["password"]
    )

    SESSION_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    await context.page.context.storage_state(path=str(SESSION_STATE_FILE))

@then("I verify overview page is loaded")
@async_run_until_complete
async def step_impl(context):
    await context.pages.parabank_page.verify_overview_page_loaded()


@then("I store the account id")
@async_run_until_complete
async def step_store_account_id(context):
    account_id = await context.pages.parabank_page.get_first_account_id()
    context.feature.account_id = account_id

@then('I visual check the page "{page_name}"')
@async_run_until_complete
async def step_visual_check_page(context, page_name):
    await context.pages.parabank_page.visual_check_page(page_name)

@then("I delete the storage state file")
@async_run_until_complete
async def step_delete_storage_state_file(context):
    await context.pages.parabank_page.delete_storage_state_file()
