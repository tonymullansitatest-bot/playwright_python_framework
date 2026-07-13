from behave import *
from behave.api.async_step import async_run_until_complete
import json
from pathlib import Path
from playwright.async_api import Error as PlaywrightError, TimeoutError as PlaywrightTimeoutError
from utils.constants import TEST_DATA_DIR
from utils.constants import PRACTICE_BASE_URL, PRACTICE_ACCOUNTS_URL, PRACTICE_OVERVIEW_URL
from sita_playwright_python_utils.config_loader import config_ini
from sita_playwright_python_utils.logger import Logger
import logging

logger = Logger(
    log_dir=config_ini.get("PATHS", "LOG_DIR"),
    log_name="ui_steps",
    log_level=logging.INFO
)


def _resolve_project_root() -> Path:
    """Find the repository root so debug paths are stable across run contexts."""
    file_path = Path(__file__).resolve()
    for parent in file_path.parents:
        if (parent / "config.ini").exists() and (parent / "src").exists():
            return parent
    return Path.cwd()


PROJECT_ROOT = _resolve_project_root()
SESSION_STATE_FILE = PROJECT_ROOT / "debug" / "practice_storage_state.json"

# Explain this test logic
# This test logic handles the login process for the practice test application.
# It first attempts to use a cached session state (cookies and local storage) to log in.
# If the session state is not available or is invalid, it performs a fresh login using credentials from a JSON file.

# Rename variables for clarity
# - `credentials_file_path` is the path to the JSON file containing user credentials.
# Add logging to track the flow of the test and any issues that arise during the login process.
logger.log("Starting login process for practice test application.")



@given("I log into practice test application")
@when("I log into practice test application")
@async_run_until_complete
async def step_practice_login(context):
    credentials_file_path = TEST_DATA_DIR / "practice_user.json"
    with open(credentials_file_path, encoding="utf-8") as f:
        data = json.load(f)

    logger.log(
        f"[STEP] Session state path: {SESSION_STATE_FILE} (exists={SESSION_STATE_FILE.exists()})"
    )

    if SESSION_STATE_FILE.exists():
        try:
            logger.log(f"Loading cached session state from {SESSION_STATE_FILE}.")
            with open(SESSION_STATE_FILE, encoding="utf-8") as f:
                state = json.load(f)

            cookies = state.get("cookies", [])
            origins = state.get("origins", [])
            if cookies:
                await context.page.context.add_cookies(cookies)
                logger.log(f"Restored {len(cookies)} cookies from cached state.")
            
            practice_origin = PRACTICE_BASE_URL
            local_storage_items = []
            for origin_entry in origins:
                if origin_entry.get("origin") == practice_origin:
                    local_storage_items = origin_entry.get("localStorage", [])
                    break
            
            await context.page.goto(PRACTICE_BASE_URL, wait_until="domcontentloaded")

            if local_storage_items:
                await context.page.evaluate(
                    """
                    (items) => {
                        for (const item of items) {
                            window.localStorage.setItem(item.name, item.value);
                        }
                    }
                    """,
                    local_storage_items,
                )

            logger.log(f"Navigate to {PRACTICE_ACCOUNTS_URL}.")
            await context.page.goto(PRACTICE_ACCOUNTS_URL, wait_until="domcontentloaded")
            await context.page.wait_for_load_state("networkidle")
            if context.page.url == PRACTICE_ACCOUNTS_URL:
                logger.log(f"Successfully logged in using cached session state.")
                return
            else:
                # If the page did not load as expected, remove the session state and perform a clean login
                logger.log("Cached session state is invalid. Performing a clean login.", log_level="warning")
                SESSION_STATE_FILE.unlink(missing_ok=True)
        except (PlaywrightError, PlaywrightTimeoutError, json.JSONDecodeError) as exc:
            logger.log(
                f"Error occurred while loading cached session state: {type(exc).__name__}: {exc}. Performing a clean login."
            )
            logging.exception("Cached session state restore failed")
            SESSION_STATE_FILE.unlink(missing_ok=True)

    await context.pages.login_page.go_to_login_page()
    await context.pages.login_page.login(
        email=data["email"],
        password=data["password"]
    )

    await context.pages.login_page.verify_login_successful()
    await context.page.wait_for_load_state("networkidle")
    logger.log("Login process completed successfully.")

    SESSION_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    await context.page.context.storage_state(path=str(SESSION_STATE_FILE))

@then("I verify user page is loaded")
@async_run_until_complete
async def step_impl(context):
    await context.pages.login_page.verify_login_successful()
    logger.log("User page loaded successfully.")

@then("I Purchase a product from the practice test application")
@async_run_until_complete
async def step_practice_purchase_product(context):
    await context.page.goto(PRACTICE_BASE_URL + "/category/hand-tools", wait_until="domcontentloaded")
    product_name = "Claw Hammer with Shock Reduction Grip"
    await context.pages.shopping_page.purchase_product(product_name)
    logger.log(f"Purchased product: {product_name}")