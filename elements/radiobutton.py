import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("RADIOBUTTON")


class Radiobutton(BaseElement):
    @property
    def type_of(self) -> str:
        return "Radiobutton"

    def select(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f"Select {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            locator.check()
        self.track_coverage(action_type=ActionType.SELECT, nth=nth, **kwargs)

    def check_selected(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f"Check {self.type_of} '{self.name}' is selected"
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_checked()
        self.track_coverage(action_type=ActionType.VALUE, nth=nth, **kwargs)
