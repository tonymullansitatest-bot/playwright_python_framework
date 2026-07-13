from datetime import date, datetime

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
import xml.etree.ElementTree as ET



@given('I send Account GET request to "{endpoint}"')
@async_run_until_complete
async def step_get_request(context, endpoint):
    # Replace {account_id} in the endpoint with the actual account ID from context
    account_id = getattr(context.feature, "account_id", None)
    endpoint = endpoint.replace("99999", str(account_id))
    context.response = await ApiUtil.get(endpoint, context.api_request)
    logger.log(f"[STEP] Response Status: {context.response.status}")
    try:
        body = await context.response.json()
    except Exception:
        body = await context.response.text()
    logger.log(f"[STEP] Response Body: {body}")

@then('the response should contain xml tag "{tag}" with value "{value}"')
@async_run_until_complete
async def step_validate_xml_tag_value(context, tag, value):
    if tag == "id":
        value = getattr(context.feature, "account_id", None)
    body = await context.response.text()
    assert f"<{tag}>{value}</{tag}>" in body, f"Expected <{tag}>{value}</{tag}> in response. Body: {body}"


@given('I deposit the following Funds POST request to "{endpoint}"')
@async_run_until_complete
async def step_deposit_funds(context, endpoint):
    account_id = getattr(context.feature, "account_id", None)
    for row in context.table:
        amount = float(row['amount'])
        params = {
            "accountId": account_id,
            "amount": amount
        }
        logger.log(f"[STEP] payload: {params}")
        context.response = await ApiUtil.post(endpoint, context.api_request, params=params)
        logger.log(f"[STEP] Response Status: {context.response.status}")
        try:
            body = await context.response.json()
        except Exception:
            body = await context.response.text()
        logger.log(f"[STEP] Response Body: {body}")
@then('The status code should be "{status_code}"')
@async_run_until_complete
async def step_validate_status_code(context, status_code):
    status_code = int(status_code)
    assert context.response.status == status_code, f"Expected status code {status_code} but got {context.response.status}"


@given('I get Account balance and customer id GET request to "{endpoint}"')
@async_run_until_complete
async def step_get_account_balance_and_customer_id(context, endpoint):
    account_id = getattr(context.feature, "account_id", None)
    endpoint = endpoint.replace("99999", str(account_id))
    context.response = await ApiUtil.get(endpoint, context.api_request)
    logger.log(f"[STEP] Response Status: {context.response.status}")
    try:
        body = await context.response.text()
    except Exception:
        body = await context.response.text()
    logger.log(f"[STEP] Response Body: {body}")

@then('I validate balance is updated and customer id is present in response "{expected_balance}"')
@async_run_until_complete
async def step_validate_balance_and_customer_id_keys(context, expected_balance):
    body = await context.response.text()
    logger.log(f"[STEP] Response Body: {body}")

    root = ET.fromstring(body)

    balance_text = root.findtext("balance")
    customer_id = root.findtext("customerId")

    expected_balance = str(getattr(context.feature, "expected_balance", expected_balance))

    assert balance_text is not None, f"Expected balance in response. Body: {body}"
    assert float(balance_text) == float(expected_balance), (
        f"Expected balance '{expected_balance}' but got '{balance_text}'. Body: {body}"
    )

    assert customer_id is not None, f"Expected customerId in response. Body: {body}"
    context.feature.customer_id = customer_id


@given('I send Clean POST request to "{endpoint}"')
@async_run_until_complete
async def step_clean_database(context, endpoint):
    context.response = await ApiUtil.post(endpoint, context.api_request)
    logger.log(f"[STEP] Response Status: {context.response.status}")
    try:
        body = await context.response.text()
    except Exception:
        body = await context.response.text()
    logger.log(f"[STEP] Response Body: {body}")


@given('I send Initialize POST request to "{endpoint}"')
@async_run_until_complete
async def step_initialize_database(context, endpoint):
    context.response = await ApiUtil.post(endpoint, context.api_request)
    logger.log(f"[STEP] Response Status: {context.response.status}")
    try:
        body = await context.response.text()
    except Exception:
        body = await context.response.text()
    logger.log(f"[STEP] Response Body: {body}")


@given('I send Transactions GET request to "{endpoint}"')
@async_run_until_complete
async def step_get_transactions(context, endpoint):
    account_id = getattr(context.feature, "account_id", None)
    endpoint = endpoint.replace("99999", str(account_id))
    context.response = await ApiUtil.get(endpoint, context.api_request)
    logger.log(f"[STEP] Response Status: {context.response.status}")
    try:
        body = await context.response.text()
    except Exception:
        body = await context.response.text()
    logger.log(f"[STEP] Response Body: {body}")

@then('I validate transactions response values')
@async_run_until_complete
async def step_validate_transactions_response_values(context):
    expected_account_id = getattr(context.feature, "account_id", None)
    body = await context.response.text()
    logger.log(f"[STEP] Transactions Response Body: {body}")

    root = ET.fromstring(body)
    assert root.tag == "transactions", f"Expected root tag 'transactions' but got '{root.tag}'. Body: {body}"

    transactions = root.findall("transaction")
    assert len(transactions) > 0, f"Expected at least one transaction. Body: {body}"

    tx = transactions[0]

    def get_text(tag):
        node = tx.find(tag)
        assert node is not None and node.text is not None, f"Expected tag '{tag}' in transaction. Body: {body}"
        return node.text.strip()

    tx_id = get_text("id")
    account_id = get_text("accountId")
    tx_type = get_text("type")
    tx_date = get_text("date")
    amount = get_text("amount")
    description = get_text("description")

    assert tx_id.isdigit() and len(tx_id) == 5, f"Expected tx_id to be a 5-digit integer but got '{tx_id}'"
    assert account_id == expected_account_id, f"Expected accountId '{expected_account_id}' but got '{account_id}'"
    assert tx_type == "Credit", f"Expected type 'Credit' but got '{tx_type}'"
    today = date.today().isoformat()
    tx_date_only = tx_date.split("T")[0]
    assert tx_date_only == today, f"Expected tx_date to be today's date '{today}' but got '{tx_date_only}'"
    assert float(amount) == 1000.00, f"Expected amount '1000.00' but got '{amount}'"
    assert description == "Deposit via Web Service", (
        f"Expected description 'Deposit via Web Service' but got '{description}'"
    )