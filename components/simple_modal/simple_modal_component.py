from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text
from tools.locators.locator_strategy import LocatorStrategy


class SimpleModalComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "#pum_popup_title_1318", "Simple Modal title",
                          locator_strategy=LocatorStrategy.CSS)
        self.description = Text(page, "div.pum-content.popmake-content", "Simple Modal description",
                                locator_strategy=LocatorStrategy.CSS)
        self.close_button = Button(page, "button.pum-close.popmake-close", "Simple Modal close button",
                                   locator_strategy=LocatorStrategy.CSS)

    def check_title(self):
        self.title.check_visible()
        self.title.check_have_text("Simple Modal")

    def check_title_not_visible(self):
        self.title.check_not_visible()

    def check_description(self):
        self.description.check_visible()
        self.description.check_have_text("Hi, I’m a simple modal.")

    def check_description_not_visible(self):
        self.description.check_not_visible()

    def check_close_button(self):
        self.close_button.check_visible()
        self.close_button.check_enabled()

    def check_close_button_not_visible(self):
        self.close_button.check_not_visible()

    def click_close_button(self):
        self.close_button.click()
