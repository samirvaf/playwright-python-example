from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

def test_login_page(base_url: str, creds: dict, page: Page) -> None:
    login = LoginPage(page)
    login.goto(base_url)
    expect(page).to_have_url(base_url)
    login.login(creds["email"], creds["password"])
    assert "Welcome, QA Engineer" in page.content()
