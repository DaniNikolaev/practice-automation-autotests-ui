import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("LINK")


class Link(BaseElement):
    @property
    def type_of(self) -> str:
        return "Link"

    def check_have_attribute(self, name: str, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f"Checking that {self.type_of} '{self.name}' has attribute '{value}'"
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_attribute(name, value)
