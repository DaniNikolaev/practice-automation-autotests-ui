import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("RADIOBUTTON")


class Radiobutton(BaseElement):
    @property
    def type_of(self) -> str:
        return "Radiobutton"

    def select(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Select {self.type_of} '{self.name}'"):
            logger.info(f"Select {self.type_of} '{self.name}'")
            locator.check()

    def check_selected(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_checked()
