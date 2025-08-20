from playwright.sync_api import Page, expect
from ui.sections.orders_section import OrdersSection
from ui.sections.samples_section import SamplesSection
from ui.sections.tests_section import TestsSection
from ui.components.toast import Toast
from ui.components.spinner import SpinnerGroup

class OrderPage:
    def __init__(self, page: Page):
        self.page = page
        self.details = OrdersSection(page)
        self.samples = SamplesSection(page)
        self.tests = TestsSection(page)
        self.toast = Toast(page.locator("body"))
        self._status_spinners = page.locator('[data-bind="visible: !loaded()"]:visible')

    def start_new_order(self, timeout: int = 20_000):
        SpinnerGroup(self._status_spinners).wait_gone(timeout=timeout)
        self.page.get_by_text("Workflow").click()
        self.page.get_by_text("Orders").click()
        self.page.get_by_role("link", name="+ New Order").click()
