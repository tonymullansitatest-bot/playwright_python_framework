"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
from behave.api.async_step import async_run_until_complete
from sita_playwright_python_utils.environment_hooks import before_all_hook, after_all_hook, before_scenario_hook, after_scenario_hook


@async_run_until_complete
async def before_all(context):
    """
    Setup to run before all tests.

    Args:
        context: Behave context object for sharing data.
    """
    await before_all_hook(context)
    context.playwright.selectors.set_test_id_attribute("data-test")
    

@async_run_until_complete
async def after_all(context):
    """
    Teardown to run after all tests.

    Args:
        context: Behave context object for shared data.
    """
    await after_all_hook(context)


@async_run_until_complete
async def before_scenario(context, scenario):
    """
    Setup to run before each scenario. Initializes the page and page objects.
    Args:
        context: Behave context object for sharing data between steps.
        scenario: The scenario object containing information about the current test scenario.
    """
    await before_scenario_hook(context, scenario)


@async_run_until_complete
async def after_scenario(context, scenario):
    """
    Teardown to run after each scenario. Stops tracing, saves videos, and attaches failed scenario screenshots.

    Args:
        context: Behave context object for sharing data between steps.
        scenario: The scenario object containing information about the current test scenario.
    """

    await after_scenario_hook(context, scenario)
