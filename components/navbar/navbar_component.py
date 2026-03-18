import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.link import Link
from tools.locators.locator_strategy import LocatorStrategy


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logo_link = Link(page, 'a.logo.logo-left', "Site logo",
                              locator_strategy=LocatorStrategy.CSS)
        self.courses_link = Link(page, "a[data-hover='Courses']", "Courses",
                                 locator_strategy=LocatorStrategy.CSS)
        self.blog_link = Link(page, "a[data-hover='Blog']", "Blog",
                              locator_strategy=LocatorStrategy.CSS)

    @allure.step("Check navbar is visible")
    def check_navbar_is_visible(self):
        self.logo_link.check_visible()
        self.courses_link.check_visible()
        self.blog_link.check_visible()

    @allure.step("Check navbar links")
    def check_navbar_links(self):
        self.logo_link.check_have_attribute("href", "https://practice-automation.com/")
        self.courses_link.check_have_attribute("href", "https://automatenow-courses.teachable.com/")
        self.blog_link.check_have_attribute("href", "https://automatenow.io/")
