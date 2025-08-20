from playwright.sync_api import Page, Locator

class Section:
    def __init__(self, page: Page, root: Locator):
        self.page = page
        self.root = root

    def within(self, selector: str) -> Locator:
        return self.root.locator(selector)
