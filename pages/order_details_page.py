from playwright.sync_api import Page


class OrderDetailsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.add_sample_button = page.get_by_role("button", name="Add Sample")
        self.add_test_button = page.get_by_role("button", name="Add Test")

    def add_sample(self, sample: dict) -> None:
        self.add_sample_button.click()
        if "name" in sample:
            self.page.get_by_label("Sample Name").fill(sample["name"])
        if "lab_id" in sample:
            self.page.get_by_label("Lab ID").fill(sample["lab_id"])
        self.page.get_by_role("button", name="Save").click()

    def add_test(self, test: dict) -> None:
        self.add_test_button.click()
        if "name" in test:
            self.page.get_by_label("Test Name").fill(test["name"])
        if "code" in test:
            self.page.get_by_label("Code").fill(test["code"])
        self.page.get_by_role("button", name="Save").click()
