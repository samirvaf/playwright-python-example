from playwright.sync_api import Page, expect

BASE_URL = "https://srqaengineer-sf-uat.qbench.net/"

def test_login_page_visual_regression(page: Page) -> None:
    page.goto(BASE_URL)
    expect(page).to_have_url(BASE_URL)
    expect(page).to_have_screenshot()
