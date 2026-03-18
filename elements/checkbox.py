import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("CHECKBOX")


class Checkbox(BaseElement):
    @property
    def type_of(self) -> str:
        return "Checkbox"

    def check(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Check {self.type_of} "{self.name}"'):
            logger.info(f'Check {self.type_of} "{self.name}"')
            locator.check()

    def uncheck(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Uncheck {self.type_of} "{self.name}"'):
            logger.info(f'Uncheck {self.type_of} "{self.name}"')
            locator.uncheck()

    def is_checked(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_checked()
