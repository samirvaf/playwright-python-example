from pathlib import Path
import sys
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from playwright.sync_api import Page, expect

from pages.orders_page import OrdersPage
from pages.order_details_page import OrderDetailsPage
from factories import make_sample


@pytest.mark.skip("requires application backend")
def test_duplicate_lab_id_error(page: Page) -> None:
    orders = OrdersPage(page)
    orders.new_order()
    details = OrderDetailsPage(page)
    first = make_sample()
    details.add_sample(first)
    details.add_sample({"lab_id": first["lab_id"], "name": "Duplicate"})
    expect(page.get_by_text("Lab ID already exists")).to_be_visible()
