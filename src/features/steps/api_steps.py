from datetime import datetime

from behave import given
from sita_playwright_python_utils.logger import Logger
from sita_playwright_python_utils.config_loader import config_ini
import logging
from utils.constants import TEST_DATA_DIR

from sita_playwright_python_utils.api_util import ApiUtil

from sita_playwright_python_utils import JsonUtil

logger = Logger(
    log_dir=config_ini.get("PATHS", "LOG_DIR"),
    log_name="api_steps",
    log_level=logging.INFO
)


from behave import then
from behave.api.async_step import async_run_until_complete
import json

from sita_playwright_python_utils.playwright_util import *

PAYLOAD_MAP = {
    "create_user": "user_create_static.json",
    "update_user_full": "user_update_full.json",
    "update_user_partial": "user_update_partial.json",
    "create_user_dynamic": "user_create_dynamic.json"
}

@given('I send GET request to "{endpoint}"')
@async_run_until_complete
async def step_get_request(context, endpoint):
    context.response = await ApiUtil.get(endpoint, context.api_request)
    logger.log(f"[STEP] Response Status: {context.response.status}")

@given('I send GET request to "{endpoint}" with query params {params}')
@async_run_until_complete
async def step_get_with_query_params(context, endpoint, params):
    query_params = json.loads(params.replace("'", '"'))
    context.response = await ApiUtil.get(endpoint, context.api_request, params=query_params)
    logger.log(f"[STEP] Response Status: {context.response.status}")



@given('I send GET request to "{endpoint}" with headers {headers}')
@async_run_until_complete
async def step_get_with_custom_headers(context, endpoint, headers):
    headers_dict = json.loads(headers.replace("'", '"'))
    context.response = await ApiUtil.get(endpoint, context.api_request, headers=headers_dict)
    logger.log(f"[STEP] Response Status: {context.response.status}")

@given('I send "{method}" request to "{endpoint}" with payload type "{payload_type}"')
@async_run_until_complete
async def step_api_with_static_payload(context, method, endpoint, payload_type):

    file_name = PAYLOAD_MAP.get(payload_type)
    if not file_name:
        raise ValueError(f"Unknown payload type: {payload_type}")

    file_path = TEST_DATA_DIR / file_name
    payload = JsonUtil.load_json_payload(str(file_path))

    context.response = await getattr(ApiUtil, method.lower())(
        endpoint,
        context.api_request,
        payload=payload
    )

    logger.log(f"[STEP] Response Status: {context.response.status}")

@given('I send "{method}" request to "{endpoint}" with dynamic payload type "{payload_type}"')
@async_run_until_complete
async def step_api_with_dynamic_payload(context, method, endpoint, payload_type):

    file_name = PAYLOAD_MAP.get(payload_type)
    if not file_name:
        raise ValueError(f"Unknown payload type: {payload_type}")

    dynamic_data = {
        "timestamp": datetime.utcnow().isoformat()
    }

    file_path = TEST_DATA_DIR / file_name
    payload = JsonUtil.load_json_payload(str(file_path), dynamic_data=dynamic_data)

    context.response = await getattr(ApiUtil, method.lower())(
        endpoint,
        context.api_request,
        payload=payload
    )

    logger.log(f"[STEP] Response Status: {context.response.status}")


@given('I send "{method}" request to "{endpoint}"')
@async_run_until_complete
async def step_api_without_payload(context, method, endpoint):

    context.response = await getattr(ApiUtil, method.lower())(
        endpoint,
        context.api_request
    )

    logger.log(f"[STEP] Response Status: {context.response.status}")


@then('the status code should be {expected_status:d}')
@async_run_until_complete
async def step_validate_status(context, expected_status):
    await ApiUtil.validate_status(context.response, expected_status)
    logger.log(f"[STEP] Status validation passed")


@then('the response should contain keys {expected_keys}')
@async_run_until_complete
async def step_validate_keys(context, expected_keys):
    keys = json.loads(expected_keys.replace("'", '"'))
    await ApiUtil.validate_keys(context.response, keys)
    logger.log(f"[STEP] Response keys validation passed")


@then('I validate GET "{endpoint}" returns {expected_status:d}')
@async_run_until_complete
async def step_validate_get(context, endpoint, expected_status):
    response = await context.api_request.get(endpoint)
    await ApiUtil.validate_status(response, expected_status)
    logger.log(f"[STEP] Validation passed for {endpoint} with status {expected_status}")
