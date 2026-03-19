import allure
from playwright.sync_api import Page

from components.footer.footer_component import FooterComponent
from components.form_modal.form_modal_component import FormModalComponent
from components.navbar.navbar_component import NavbarComponent
from components.simple_modal.simple_modal_component import SimpleModalComponent
from components.title_and_breadcrumbs.title_and_breadcrumbs_component import TitleAndBreadcrumbsComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage
from tools.locators.locator_strategy import LocatorStrategy


class ModalsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.title_and_breadcrumbs = TitleAndBreadcrumbsComponent(page, "Modals")
        self.main_description = Text(page, "p.wp-block-paragraph >> nth=0", "Modals main description",
                                     locator_strategy=LocatorStrategy.CSS)
        self.additional_description = Text(page, "p:has(strong)", "Modals additional description",
                                           locator_strategy=LocatorStrategy.CSS)
        self.simple_modal_label = Text(page, "p.wp-block-paragraph >> nth=2", "Modals simple modal label",
                                       locator_strategy=LocatorStrategy.CSS)
        self.simple_modal_button = Button(page, "#simpleModal", "Modals simple modal button",
                                          locator_strategy=LocatorStrategy.CSS)
        self.simple_modal = SimpleModalComponent(page)
        self.form_modal_label = Text(page, "p.wp-block-paragraph >> nth=3", "Modals form modal label",
                                     locator_strategy=LocatorStrategy.CSS)
        self.form_modal_button = Button(page, "#formModal", "Modals form modal button",
                                        locator_strategy=LocatorStrategy.CSS)
        self.form_modal = FormModalComponent(page)
        self.footer = FooterComponent(page)

    @allure.step("Check modals title and breadcrumbs")
    def check_title_and_breadcrumbs(self):
        self.title_and_breadcrumbs.check_breadcrumbs_title()
        self.title_and_breadcrumbs.check_page_title()
        self.title_and_breadcrumbs.check_home_link()

    def check_description(self):
        self.main_description.check_visible()
        self.main_description.check_have_text("Many websites like using modal to grab the user’s attention. A modal "
                                              "is a special type of dialog that is used to present the user with some "
                                              "information or to get data from the end user of an application. Choose "
                                              "from the options below to learn how to automate modals.")
        self.additional_description.check_visible()
        self.additional_description.check_have_text("IMPORTANT: Please ensure that ad blockers are turned OFF in your "
                                                    "browser. Otherwise, you won’t see the modals.")

    def check_simple_modal_label(self):
        self.simple_modal_label.check_visible()
        self.simple_modal_label.check_have_text("Click to see a simple modal.")

    def check_form_modal_label(self):
        self.form_modal_label.check_visible()
        self.form_modal_label.check_have_text("Click to see a modal that contains a form.")

    def click_simple_modal_button(self):
        self.simple_modal_button.click()

    def click_form_modal_button(self):
        self.form_modal_button.click()

    def check_simple_modal_button(self):
        self.simple_modal_button.check_visible()
        self.simple_modal_button.check_enabled()

    def check_form_modal_button(self):
        self.form_modal_button.check_visible()
        self.form_modal_button.check_enabled()

    @allure.step("Check modals simple modal")
    def check_simple_modal(self):
        self.simple_modal.check_title()
        self.simple_modal.check_description()
        self.simple_modal.check_close_button()

    @allure.step("Check modals simple modal is not visible")
    def check_simple_modal_not_visible(self):
        self.simple_modal.check_title_not_visible()
        self.simple_modal.check_description_not_visible()
        self.simple_modal.check_close_button_not_visible()

    @allure.step("Check modals form modal")
    def check_form_modal(self):
        self.form_modal.check_title()
        self.form_modal.check_description()
        self.form_modal.check_close_button()
        self.form_modal.check_back_link()
        self.form_modal.check_form_title()
        self.form_modal.check_form()
        self.form_modal.check_after_form()
        self.form_modal.check_submit_button()

    @allure.step("Check modals form modal is not visible")
    def check_form_modal_not_visible(self):
        self.form_modal.check_title_not_visible()
        self.form_modal.check_description_not_visible()
        self.form_modal.check_close_button_not_visible()
        self.form_modal.check_back_link_not_visible()
        self.form_modal.check_form_title_not_visible()
        self.form_modal.check_form_not_visible()
        self.form_modal.check_name_required_not_visible()
        self.form_modal.check_after_form_not_visible()
        self.form_modal.check_submit_button_not_visible()
