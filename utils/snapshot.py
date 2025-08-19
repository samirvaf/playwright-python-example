from typing import Iterable
from playwright.sync_api import Locator, Page, expect


def snapshot(page: Page, name: str, masks: Iterable[Locator] | None = None) -> None:
    expect(page).to_have_screenshot(name=name, mask=list(masks or []))
