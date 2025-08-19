import re
from playwright.sync_api import Locator, Page, expect


def _normalize(name: str) -> str:
    return re.sub(r"\s+", " ", name).strip()


def order_row(page: Page, name: str) -> Locator:
    normalized = _normalize(name)
    pattern = re.compile(re.sub(r"\s+", r"\\s+", re.escape(normalized)), re.I)
    return page.get_by_role("row", name=pattern)


def open_order_row(page: Page, name: str) -> Locator:
    row = order_row(page, name)
    row.get_by_role("link", name=re.compile("view|details", re.I)).click()
    return row


def delete_order_by_name(page: Page, name: str) -> None:
    row = order_row(page, name)
    row.get_by_role("button", name=re.compile("menu|more|actions", re.I)).click()
    page.get_by_role("menuitem", name=re.compile("delete", re.I)).click()
    page.get_by_role("button", name=re.compile("confirm|delete", re.I)).click()
    expect(page.get_by_role("alert")).to_contain_text(re.compile("deleted|success", re.I))
