from playwright.sync_api import Page
from helpers.orders import open_order_row


class OrdersPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.new_order_button = page.get_by_role("button", name="New Order")

    def new_order(self) -> None:
        self.new_order_button.click()

    def open_order(self, name: str) -> None:
        open_order_row(self.page, name)
