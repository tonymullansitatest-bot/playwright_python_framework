"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
import logging

from behave import *
from behave.api.async_step import async_run_until_complete
from playwright.async_api import expect

from sita_playwright_python_utils import logger
from sita_playwright_python_utils.OctaneUtility import update_test_run_status
from src.pages.pages import Pages


@given("The user is on the demo page")
@async_run_until_complete
async def step_impl(context):
    await context.page.goto(context.base_url)


@when("The user navigates to the elements page")
@async_run_until_complete
async def step_impl(context):
    await context.pages.gherkin_examples_page.click_elements_menu_option()


@then("The text box option is displayed")
@async_run_until_complete
async def step_impl(context):
    await expect(context.pages.gherkin_examples_page.text_box_option).to_be_visible()

@then('The practice form option is displayed')
@async_run_until_complete
async def step_impl(context):
    await expect(context.pages.gherkin_examples_page.practice_form_option).to_be_visible()


@when("The user navigates to the forms page")
@async_run_until_complete
async def step_impl(context):
    pages = Pages(context)
    await pages.gherkin_examples_page.click_forms_menu_option()


@when("The user navigates to the text box page")
@async_run_until_complete
async def step_impl(context):
    await context.pages.gherkin_examples_page.click_text_box_option()


@when('Fill the full name with "{name}"')
@async_run_until_complete
async def step_impl(context, name):
    await context.pages.gherkin_examples_page.fill_full_name(name)


@when("Submits the form")
@async_run_until_complete
async def step_impl(context):
    await context.pages.gherkin_examples_page.click_submit_button()


@then('The name "{name}" is displayed')
@async_run_until_complete
async def step_impl(context, name):
    await expect(context.pages.gherkin_examples_page.submitted_data).to_contain_text(name)


@when("Fill the description with")
@async_run_until_complete
async def step_impl(context):
    description = context.text
    await context.pages.gherkin_examples_page.fill_description(description)
    # saving data to the context to be used in other steps
    context.description = description


@then("The description data are displayed")
@async_run_until_complete
async def step_impl(context):
    await expect(context.pages.gherkin_examples_page.submitted_data).to_contain_text(context.description)


@when("Fill the form with the following data")
@async_run_until_complete
async def step_impl(context):
    data = context.table
    for row in data:
        await context.pages.gherkin_examples_page.fill_full_name(row["Full Name"])
        await context.pages.gherkin_examples_page.fill_email(row["Email Address"])
        await context.pages.gherkin_examples_page.fill_current_address(row["Current Address"])


@then("The data are displayed")
@async_run_until_complete
async def step_impl(context):
    data = await context.pages.gherkin_examples_page.submitted_data.inner_text()
    assert len(data) > 20
