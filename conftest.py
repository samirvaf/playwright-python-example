import os
import pytest
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from playwright.sync_api import Page, Locator, expect

load_dotenv()

@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ["BASE_URL"]

@pytest.fixture
def creds():
    return {
        "email": os.environ["USER_EMAIL"],
        "password": os.environ["USER_PASSWORD"],
    }

def mask_common(page: Page) -> List[Locator]:
    return [
        page.get_by_text("Created at", exact=False),
        page.get_by_text("Updated at", exact=False),
        page.get_by_text("Order #", exact=False),
        page.locator("img[alt*=avatar]"),
    ]

@pytest.fixture
def snapshot(page: Page):
    def take(name: str, masks: List[Locator] = None):
        expect(page).to_have_screenshot(
            name=name,
            mask=masks or [],
            max_diff_pixels=0,
        )
    return take
