from playwright.sync_api import Page, Locator, expect
from .base_section import Section
from ui.components.spinner import SpinnerGroup

class OrdersSection(Section):
    def __init__(self, page: Page):
        root = page.locator("[role='tabpanel']#details")
        super().__init__(page, root)

        self._order_spinner  = page.locator("#qbenchOrderSpinnerDiv:visible")
        self._samples_spinner = page.locator("#qbenchOrderSamplesSpinnerDiv")

    # --- Locators ---
    @property
    def select_customer_dropdown(self) -> Locator:
        return self.root.get_by_role("link", name="Select Customer")

    @property
    def select_user_dropdown(self) -> Locator:
        return self.root.get_by_role("link", name="Select User")

    @property
    def save_order_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Save Order")

    @property
    def status_created(self) -> Locator:
        return self.page.get_by_role("link", name="CREATED")

    # --- Actions ---
    def choose_customer(self, label: str):
        self.select_customer_dropdown.click()
        self.page.get_by_role("option", name=label).click()

    def choose_user(self, label: str = "QA Engineer"):
        self.page.get_by_role("link", name=" special fields").click()
        self.select_user_dropdown.click()
        self.page.get_by_role("option", name=label).click()

    def save(self, timeout: int = 20_000):
        self.save_order_btn.click()
        self.save_order_btn.wait_for(state="detached", timeout=timeout)
        SpinnerGroup(self._order_spinner, self._samples_spinner).wait_gone(timeout=timeout)
