from playwright.sync_api import Locator, expect

class Toast:
    def __init__(self, scope: Locator):
        self.scope = scope

    def expect_text(self, text: str, timeout: int = 10_000):
        expect(self.scope.get_by_text(text)).to_be_visible(timeout=timeout)
