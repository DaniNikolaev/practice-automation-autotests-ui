# elements/slider.py
import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement, LocatorStrategy
from tools.logger import get_logger
from ui_coverage_tool import ActionType

logger = get_logger("SLIDER")


class Slider(BaseElement):

    @property
    def type_of(self) -> str:
        return "Slider"

    def set_value(self, value: int, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Setting {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):
            logger.info(step)

            locator.evaluate(f"el => el.value = {value}")

            locator.evaluate("el => el.dispatchEvent(new Event('input', { bubbles: true }))")
            locator.evaluate("el => el.dispatchEvent(new Event('change', { bubbles: true }))")

        self.track_coverage(action_type=ActionType.FILL, nth=nth, value=value, **kwargs)

    def get_value(self, nth: int = 0, **kwargs) -> int:
        locator = self.get_locator(nth, **kwargs)
        step = f'Getting current value from {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            value_str = locator.get_attribute("value") or "0"
            return int(value_str)

    def check_value(self, expected_value: int, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has value "{expected_value}"'
        with allure.step(step):
            logger.info(step)
            actual = self.get_value(nth, **kwargs)
            assert actual == expected_value, \
                f"Expected slider value {expected_value}, but got {actual}"

        self.track_coverage(action_type=ActionType.VALUE, nth=nth, expected=expected_value, **kwargs)
