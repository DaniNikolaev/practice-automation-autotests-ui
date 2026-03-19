import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.link import Link
from elements.text import Text
from tools.locators.locator_strategy import LocatorStrategy


class FooterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.learn_more_link = Link(page, 'Learn More', "Learn More", LocatorStrategy.TEXT)
        self.about_link = Link(page, 'About', "About", LocatorStrategy.TEXT)
        self.copyright_text = Text(page, '#copyright', "Copyright", LocatorStrategy.CSS)
        self.to_top_link = Link(page, '#to-top', "To top", LocatorStrategy.CSS)

    @allure.step("Check footer is visible")
    def check_footer_visible(self):
        self.learn_more_link.check_visible()
        self.about_link.check_visible()
        self.copyright_text.check_visible()
        self.to_top_link.check_visible()

    @allure.step("Check footer text")
    def check_footer_text(self):
        self.learn_more_link.check_have_text("Learn More")
        self.about_link.check_have_text("About")
        self.copyright_text.check_have_text("© 2020-2026 - automateNow, LLC. All rights reserved.")

    @allure.step("Check footer links")
    def check_footer_links(self):
        self.learn_more_link.check_have_attribute("href", "https://linktr.ee/automateNow")
        self.about_link.check_have_attribute("href", "https://automatenow.io/about/")
        self.to_top_link.check_have_attribute("href", "#body")

    def click_learn_more_link(self):
        self.learn_more_link.click()

    def click_about_link(self):
        self.about_link.click()
