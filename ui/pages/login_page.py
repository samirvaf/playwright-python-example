from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def welcome_message(self) -> Locator:
        return self.page.get_by_text("Welcome, QA Engineer!")

    def goto(self, base_url: str):
        self.page.goto(base_url)

    def login(self, email: str, password: str):
        self.page.get_by_placeholder("Email").fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Log in").click()
