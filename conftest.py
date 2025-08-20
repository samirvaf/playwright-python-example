import os
import pytest
from dotenv import load_dotenv

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

@pytest.fixture(autouse=True)
def stable_viewport(page):
    page.set_viewport_size({"width": 1280, "height": 900})
    page.emulate_media(color_scheme="light")
