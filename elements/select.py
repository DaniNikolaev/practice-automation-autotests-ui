import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("SELECT")


class Select(BaseElement):
    @property
    def type_of(self) -> str:
        return "Select"

    def select_by_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f"Select option with value {value} in {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            locator.select_option(value=value)

    def get_selected_value(self, nth: int = 0, **kwargs) -> str:
        locator = self.get_locator(nth, **kwargs)
        step = f"Get selected value from {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            return locator.input_value()

    def check_selected_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f"Select option with value {value} in {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_value(value)
