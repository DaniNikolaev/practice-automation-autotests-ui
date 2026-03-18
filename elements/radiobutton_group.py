from typing import Dict, Optional
from playwright.sync_api import Page
import allure

from elements.radiobutton import Radiobutton
from tools.logger import get_logger

logger = get_logger("RADIOBUTTON_GROUP")


class RadiobuttonGroup:
    def __init__(self, page: Page, options: Dict[str, str]):
        self.page = page
        self.radiobuttons = {}

        for option_name, test_id in options.items():
            self.radiobuttons[option_name] = Radiobutton(
                page, test_id, f"Radio {option_name}"
            )

    def select(self, option_name: str):
        self.radiobuttons[option_name].select()

    def check_selected(self, option_name: str):
        self.radiobuttons[option_name].check_selected()

    def check_visible(self):
        for radiobutton in self.radiobuttons.values():
            radiobutton.check_visible()


