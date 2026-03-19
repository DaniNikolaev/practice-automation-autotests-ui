import allure
from playwright.sync_api import Page

from components.footer.footer_component import FooterComponent
from components.navbar.navbar_component import NavbarComponent
from pages.base_page import BasePage
from elements.button import Button
from elements.text import Text
from tools.locators.locator_strategy import LocatorStrategy


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.title = Text(page, 'h1.wp-block-heading', "Main page title",
                          locator_strategy=LocatorStrategy.CSS)
        self.description = Text(page, 'p.wp-block-paragraph', "Main page description",
                                locator_strategy=LocatorStrategy.CSS)

        self.forms_button = Button(page, 'Form Fields', "Form fields button",
                                   locator_strategy=LocatorStrategy.TEXT)
        self.events_button = Button(page, 'Click Events', "Click events button",
                                    locator_strategy=LocatorStrategy.TEXT)
        self.popups_button = Button(page, 'Popups', "Popups button",
                                    locator_strategy=LocatorStrategy.TEXT)
        self.slider_button = Button(page, 'Sliders', "Slider button",
                                    locator_strategy=LocatorStrategy.TEXT)
        self.modals_button = Button(page, 'Modals', "Modals button",
                                    locator_strategy=LocatorStrategy.TEXT)

        self.footer = FooterComponent(page)

    def check_title(self):
        self.title.check_visible()
        self.title.check_have_text("Welcome to your software automation practice website!")

    def check_description(self):
        self.description.check_visible()
        self.description.check_have_text("We have developed this site as a one-stop place to practice web automation. "
                                         "You can find additional software automated testing, and other resources on "
                                         "our parent website.")

    def click_forms_button(self):
        self.forms_button.click()

    def check_forms_button(self):
        self.forms_button.check_visible()
        self.forms_button.check_enabled()

    def click_events_button(self):
        self.events_button.click()

    def check_events_button(self):
        self.events_button.check_visible()
        self.events_button.check_enabled()

    def click_popups_button(self):
        self.popups_button.click()

    def check_popups_button(self):
        self.popups_button.check_visible()
        self.popups_button.check_enabled()

    def click_slider_button(self):
        self.slider_button.click()

    def check_slider_button(self):
        self.slider_button.check_visible()
        self.slider_button.check_enabled()

    def click_modals_button(self):
        self.modals_button.click()

    def check_modals_button(self):
        self.modals_button.check_visible()
        self.modals_button.check_enabled()
