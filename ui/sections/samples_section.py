from playwright.sync_api import Page, Locator, expect
from .base_section import Section
from ui.components.spinner import SpinnerGroup

class SamplesSection(Section):
    def __init__(self, page: Page):
        root = page.locator("#qbenchOrderSamplesRowView")
        super().__init__(page, root)
        self._order_spinner   = page.locator("#qbenchOrderSpinnerDiv:visible")
        self._samples_spinner = page.locator("#qbenchOrderSamplesSpinnerDiv:visible")
        self._tests_spinner   = page.locator("#qbenchOrderTestsSpinnerDiv:visible")

    # --- Locators ---
    @property
    def create_new_samples_btn(self) -> Locator:
        return self.page.get_by_role("button", name="+ Create New Samples")

    @property
    def number_of_samples(self) -> Locator:
        return self.page.get_by_role("textbox", name="Number of Samples")

    @property
    def add_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Add")

    @property
    def save_samples_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Save Samples")

    def lab_id_input(self) -> Locator:
        return self.page.locator('[data-attr-name="lab_id"]')

    def sample_type_input(self) -> Locator:
        return self.page.locator('[data-attr-name="sample_type"]')

    def description_input(self) -> Locator:
        return self.page.locator('[data-attr-name="description"]')

    def time_of_collection_input(self) -> Locator:
        return self.page.locator('[data-attr-name="time_of_collection"]')

    def point_of_collection_input(self) -> Locator:
        return self.page.locator('[data-attr-name="point_of_collection"]')

    @property
    def created_sample_row_link(self) -> Locator:
        tbody = self.page.locator("#qbenchOrderLoggingSampleTbody")
        return tbody.locator('[data-bind="attr: { href: sample_detail_url }, text: display_id"]')

    # --- Actions ---
    def create_one_sample(self):
        self.create_new_samples_btn.click()
        self.number_of_samples.fill("1")
        self.add_btn.click()

    def fill_sample_fields(self, *, lab_id: str, sample_type: str, description: str, day: str, point: str):
        self.lab_id_input().fill(lab_id)
        self.sample_type_input().fill(sample_type)
        self.description_input().fill(description)
        self.time_of_collection_input().click()
        self.page.get_by_role("cell", name=day, exact=True).click()
        self.point_of_collection_input().fill(point)

    def save(self, timeout: int = 20_000):
        self.save_samples_btn.click()
        SpinnerGroup(self._order_spinner, self._samples_spinner, self._tests_spinner).wait_gone(timeout=timeout)
