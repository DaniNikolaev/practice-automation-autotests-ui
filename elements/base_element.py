from ui_coverage_tool import ActionType, SelectorType

#from elements.ui_coverage import tracker
from tools.logger import get_logger
from tools.locators.locator_strategy import LocatorStrategy

import allure
from playwright.sync_api import Page, expect, Locator


logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str, locator_strategy: str = LocatorStrategy.TEST_ID):
        self.page = page
        self.locator = locator
        self.name = name
        self.strategy = locator_strategy

    @property
    def type_of(self) -> str:
        return "base_element"

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        locator = self.locator.format(**kwargs)

        if self.strategy == LocatorStrategy.TEST_ID:
            return f"//*[@data-testid='{locator}'][{nth + 1}]"
        elif self.strategy == LocatorStrategy.CSS:
            return f"css={locator}"
        elif self.strategy == LocatorStrategy.XPATH:
            return f"xpath={locator}"
        elif self.strategy == LocatorStrategy.TEXT:
            return f"text={locator}"
        elif self.strategy == LocatorStrategy.ROLE:
            return f"role={locator}"
        elif self.strategy == LocatorStrategy.LABEL:
            return f"label={locator}"
        elif self.strategy == LocatorStrategy.PLACEHOLDER:
            return f"placeholder={locator}"
        elif self.strategy == LocatorStrategy.ALT_TEXT:
            return f"alt={locator}"
        elif self.strategy == LocatorStrategy.TITLE:
            return f"title={locator}"
        else:
            return locator

    # def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs):
    #     tracker.track_coverage(selector=self.get_raw_locator(nth, **kwargs),
    #                            action_type=action_type,
    #                            selector_type=SelectorType.XPATH)

    def get_playwright_locator(self, locator: str, **kwargs) -> Locator:
        formatted_locator = locator.format(**kwargs)

        if self.strategy == LocatorStrategy.TEST_ID:
            return self.page.get_by_test_id(formatted_locator)
        elif self.strategy == LocatorStrategy.CSS:
            return self.page.locator(f"css={formatted_locator}")
        elif self.strategy == LocatorStrategy.XPATH:
            return self.page.locator(f"xpath={formatted_locator}")
        elif self.strategy == LocatorStrategy.TEXT:
            return self.page.get_by_text(formatted_locator, exact=False)
        elif self.strategy == LocatorStrategy.ROLE:
            # Для role можно добавить дополнительные параметры
            return self.page.get_by_role(formatted_locator)
        elif self.strategy == LocatorStrategy.LABEL:
            return self.page.get_by_label(formatted_locator)
        elif self.strategy == LocatorStrategy.PLACEHOLDER:
            return self.page.get_by_placeholder(formatted_locator)
        elif self.strategy == LocatorStrategy.ALT_TEXT:
            return self.page.get_by_alt_text(formatted_locator)
        elif self.strategy == LocatorStrategy.TITLE:
            return self.page.get_by_title(formatted_locator)
        else:
            # По умолчанию используем CSS
            return self.page.locator(formatted_locator)

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with {self.strategy}="{locator}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            playwright_locator = self.get_playwright_locator(self.locator, **kwargs)
            return playwright_locator.nth(nth)

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Clicking {self.type_of} "{self.name}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            locator.click()

        #self.track_coverage(action_type=ActionType.CLICK, nth=nth, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" is visible"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_visible()

        #self.track_coverage(action_type=ActionType.VISIBLE, nth=nth, **kwargs)

    def check_not_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" is not visible"'
        with allure.step(step):
            logger.info(step)
            expect(locator).not_to_be_visible()

        #self.track_coverage(action_type=ActionType.VISIBLE, nth=nth, **kwargs)

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" has text "{text}"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_text(text)

        #self.track_coverage(action_type=ActionType.TEXT, nth=nth, **kwargs)
