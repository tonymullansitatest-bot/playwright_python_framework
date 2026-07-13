"""Copyright © SITA Information Networking Computing UK Ltd 2022-2026 Confidential.All rights reserved."""
from pathlib import Path

# Get the base directory where this constants file is located
BASE_DIR = Path(__file__).resolve().parent

# Project root
PROJECT_ROOT = BASE_DIR.parent

# Test data directory
TEST_DATA_DIR = BASE_DIR.parent / "src" / "test_data"

EXCEL_DEMO_FILE = BASE_DIR / "excel.xlsx"
EXCEL_DEFAULT_SHEET = "Sheet1"

##azure constants##
AIRLINE_URL = "https://mybag-qa.aero/baggage/#/pax/aireuropa/en-gb/main-menu"
HOMEPAGE_URL = "https://mybag-qa.aero/baggage/#/pax"
ALERT_URL = "https://demoqa.com/alerts"
HOVER_OVER_URL = "https://seleniumbase.io/demo_page"
AIRLINE_Name = "Air Europa"
HOMEPAGE_HEADER = "Report and track your baggage if it’s missing or delayed."
PAGE_TITLE = "Self Service UI"


PRACTICE_BASE_URL = "https://practicesoftwaretesting.com"
PRACTICE_OVERVIEW_URL = f"{PRACTICE_BASE_URL}/overview.htm"
PRACTICE_ACCOUNTS_URL = f"{PRACTICE_BASE_URL}/account"
