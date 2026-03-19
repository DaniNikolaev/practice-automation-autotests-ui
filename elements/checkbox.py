import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("CHECKBOX")


class Checkbox(BaseElement):
    @property
    def type_of(self) -> str:
        return "Checkbox"

    def check(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f"Check {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            locator.check()

        self.track_coverage(action_type=ActionType.CHECKED, nth=nth, **kwargs)

    def uncheck(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f"Uncheck {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            locator.uncheck()

        self.track_coverage(action_type=ActionType.UNCHECKED, nth=nth, **kwargs)

    def is_checked(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f"Check that {self.type_of} '{self.name}' is checked"
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_checked()
        self.track_coverage(action_type=ActionType.VALUE, nth=nth, **kwargs)
