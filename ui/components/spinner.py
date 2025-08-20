from playwright.sync_api import Locator, expect

class SpinnerGroup:
    """
    Waits for known spinners.
    Provide only the ones that matter for the action you just triggered.
    """
    def __init__(self, *spinners: Locator):
        self._spinners = spinners

    def wait_gone(self, timeout: int = 10_000):
        for sp in self._spinners:
            expect(sp).to_have_count(0, timeout=timeout)
