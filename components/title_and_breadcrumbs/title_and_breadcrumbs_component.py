import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.link import Link
from elements.text import Text
from tools.locators.locator_strategy import LocatorStrategy


class TitleAndBreadcrumbsComponent(BaseComponent):
    def __init__(self, page: Page, page_name: str):
        super().__init__(page)

        self.page_title = Text(page, 'heading', "Page title", locator_strategy=LocatorStrategy.ROLE)
        self.home_link = Link(page, 'Home', "Courses", locator_strategy=LocatorStrategy.TEXT)
        self.breadcrumbs_title = Text(page, "[aria-current='page']", "Breadcrumbs title",
                                      locator_strategy=LocatorStrategy.CSS)
        self.page_name = page_name

    def check_page_title(self):
        self.page_title.check_visible()
        self.page_title.check_have_text(self.page_name)

    def click_home_link(self):
        self.home_link.click()

    def check_home_link(self):
        self.home_link.check_visible()
        self.home_link.check_have_attribute("href", "https://practice-automation.com/")

    def check_breadcrumbs_title(self):
        self.breadcrumbs_title.check_visible()
        self.breadcrumbs_title.check_have_text(self.page_name)
