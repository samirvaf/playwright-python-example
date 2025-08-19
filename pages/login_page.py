from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.email = page.get_by_placeholder("Email")
        self.password = page.get_by_placeholder("Password")
        self.submit = page.get_by_role("button", name="Log In")

    def goto(self, base_url: str):
        self.page.goto(f"{base_url}")

    def login(self, email: str, password: str) -> None:
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()
