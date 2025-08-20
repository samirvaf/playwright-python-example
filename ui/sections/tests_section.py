from playwright.sync_api import Page, Locator, expect
from .base_section import Section
from ui.components.spinner import SpinnerGroup

class TestsSection(Section):
    def __init__(self, page: Page):
        root = page.locator("#qbenchOrderTestAssignmentDiv")
        super().__init__(page, root)
        self._tests_spinner = page.locator("#qbenchOrderTestsSpinnerDiv")

    # --- Locators ---
    @property
    def assign_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Assign")

    @property
    def move_right_btn(self) -> Locator:
        return self.page.get_by_role("button", name="")

    @property
    def save_tests_btn(self) -> Locator:
        return self.page.get_by_role("button", name="Save Tests")
    
    @property
    def test_id(self) -> Locator:
        return self.page.locator('[data-bind="attr: { href: test_detail_url }, text: id"]')

    def selectable_list(self) -> Locator:
        return self.page.locator('[id="-704891427-selectable"]')

    def all_scopes_checkbox(self) -> Locator:
        return self.page.locator('input[name="all_scopes_section"]')

    # --- Actions ---
    def choose_assignee(self, name: str):
        self.page.get_by_role("link", name="--Select--").click()
        self.page.get_by_role("option", name=name).click()
    
    def add_test(self, assay_name: str = "- Amino Acids", assignee: str = "QA Engineer", timeout: int = 20_000):
        self.selectable_list().get_by_text(assay_name).click()
        self.move_right_btn.click()
        self.assign_btn.click()
        self.all_scopes_checkbox().check()
        self.page.get_by_role("button", name="Submit").click()
        self.choose_assignee(assignee)
        self.save_tests_btn.click()
