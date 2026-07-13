
from behave import given
from behave import then
from behave.api.async_step import async_run_until_complete
import logging
from sita_playwright_python_utils.api_util import ApiUtil
from sita_playwright_python_utils.logger import Logger
from sita_playwright_python_utils.config_loader import config_ini
from utils.utils import _decode_jwt_payload

logger = Logger(
    log_dir=config_ini.get("PATHS", "LOG_DIR"),
    log_name="api_steps",
    log_level=logging.INFO
)


@given('I send Practice GET request to "{endpoint}"')
@async_run_until_complete
async def step_get_products(context, endpoint):
    context.response = await ApiUtil.get(endpoint, context.api_request)
    logger.log(f"[STEP] Response Status: {context.response.status}")
    try:
        body = await context.response.text()
    except Exception:
        body = await context.response.text()
    logger.log(f"[STEP] Response Body: {body}")


@then('the response should contain Thor Hammer with price 11.14')
@async_run_until_complete
async def step_verify_product_response_contains(context):
    apr_url = "https://api.practicesoftwaretesting.com"
    body = await context.response.json()
    items = body.get("data", [])
    assert items, f"Expected non-empty 'data' list, got: {body}"
    productId = items[0]["id"]
    context.response = await ApiUtil.get(f"{apr_url}/products/{productId}", context.api_request)
    assert context.response.status == 200, f"Expected status code 200 but got {context.response.status}"
    body = await context.response.json()
    assert body["in_stock"] == True, f"Expected In stock to be True but got {body['in_stock']}"
    assert body["is_location_offer"] == False, f"Expected is_location_offer to be False but got {body['is_location_offer']}"
    assert body["price"] == 11.14, f"Expected price to be 11.14 but got {body['price']}"
    assert body["name"] == "Thor Hammer", f"Expected name to be 'Thor Hammer' but got {body['name']}"


@then("I confirm JWT Token is Valid")
@async_run_until_complete
async def step_confirm_jwt_token_valid(context):
    # Check if the JWT token is present in local storage
    jwt_token = await context.page.evaluate("() => window.localStorage.getItem('auth-token')")
    assert jwt_token is not None, "JWT token not found in local storage"

    claims = _decode_jwt_payload(jwt_token)
    logger.log(f"Decoded JWT claims: {claims}")

    assert claims.get("role") == 'user', f"Expected role='user', got {claims.get('role')}"
    assert claims.get("iss") == 'https://api.practicesoftwaretesting.com/users/login', f"Expected iss='https://api.practicesoftwaretesting.com/users/login', got {claims.get('iss')}"
    assert "exp" in claims, "Missing exp claim"