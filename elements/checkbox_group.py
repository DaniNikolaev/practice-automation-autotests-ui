from typing import List, Dict
from playwright.sync_api import Page
import allure

from elements.checkbox import Checkbox
from tools.logger import get_logger

logger = get_logger("CHECKBOX_GROUP")


class CheckboxGroup:
    def __init__(self, page: Page, options: Dict[str, str]):
        self.page = page
        self.checkboxes = {}

        for option_name, test_id in options.items():
            self.checkboxes[option_name] = Checkbox(
                page, test_id, f"Checkbox {option_name}"
            )

    def check(self, option_name: str):
        self.checkboxes[option_name].check()

    def uncheck(self, option_name: str):
        self.checkboxes[option_name].uncheck()

    def check_checked(self, option_name: str):
        self.checkboxes[option_name].is_checked()

    def check_visible(self):
        for checkbox in self.checkboxes.values():
            checkbox.check_visible()
