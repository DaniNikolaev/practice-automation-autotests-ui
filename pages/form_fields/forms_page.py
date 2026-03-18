import allure
from playwright.sync_api import Page

from components.footer.footer_component import FooterComponent
from components.navbar.navbar_component import NavbarComponent
from components.title_and_breadcrumbs.title_and_breadcrumbs_component import TitleAndBreadcrumbsComponent
from elements.checkbox_group import CheckboxGroup
from elements.input import Input
from elements.radiobutton_group import RadiobuttonGroup
from elements.select import Select
from elements.textarea import Textarea
from pages.base_page import BasePage
from elements.button import Button
from elements.text import Text
from tools.locators.locator_strategy import LocatorStrategy


class FormsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.title_and_breadcrumbs = TitleAndBreadcrumbsComponent(page, "Form Fields")
        self.description_text = Text(page, "p.wp-block-paragraph", "Description",
                                     locator_strategy=LocatorStrategy.CSS)
        self.name_input = Input(page, 'name-input', "Name")
        self.password_input = Input(page, "Password", "Password",
                                    locator_strategy=LocatorStrategy.LABEL)
        self.drink_checkbox_group = CheckboxGroup(page,
                                                  {
                                                      'Water': "drink1",
                                                      'Milk': "drink2",
                                                      'Coffee': "drink3",
                                                      'Sode': "drink4",
                                                      'Tea': "drink5",
                                                  }
                                                  )
        self.color_radiobutton_group = RadiobuttonGroup(page,
                                                        {
                                                            'Red': "color1",
                                                            'Blue': "color2",
                                                            'Yellow': "color3",
                                                            'Green': "color4",
                                                            '#FFC0CB': "color5",
                                                         })
        self.automation_select = Select(page, 'automation', "Automation")
        self.email_input = Input(page, 'email', "Email")
        self.message_textarea = Textarea(page, 'message', "Message")
        self.submit_button = Button(page, 'submit-btn', "Submit")
        self.footer = FooterComponent(page)

    @allure.step("Check form_field page title and breadcrumbs")
    def check_title_and_breadcrumbs(self):
        self.title_and_breadcrumbs.check_breadcrumbs_title()
        self.title_and_breadcrumbs.check_page_title()
        self.title_and_breadcrumbs.check_home_link()

    @allure.step("Check form_fields page description")
    def check_description(self):
        self.description_text.check_visible()
        self.description_text.check_have_text("Filling out a web form is one of the most "
                                              "fundamental things to learn as you begin "
                                              "your automation journey. You can use the "
                                              "following form to practice entering text "
                                              "into an input field (here is how to enter "
                                              "text using Cypress), selecting a checkbox, "
                                              "clicking a radio button, selecting from a "
                                              "drop-down menu, getting an element’s text and "
                                              "other similar things. Have fun!")

    def fill_name(self, name: str = "test"):
        self.name_input.fill(name)

    def fill_password(self, password: str = "pass"):
        self.password_input.fill(password)

    def select_checkboxes(self, checkboxes_name: list[str] | None = None):
        if checkboxes_name is None:
            checkboxes_name = ["Water"]
        for name in checkboxes_name:
            self.drink_checkbox_group.check(name)

    def select_radiobutton(self, radiobutton: str = "Red"):
        self.color_radiobutton_group.select(radiobutton)

    def select_option(self, value: str = "yes"):
        self.automation_select.select_by_value(value)

    def fill_email(self, email: str = "test@test.com"):
        self.email_input.fill(email)

    def fill_message(self, message: str = "Test message"):
        self.message_textarea.fill(message)

    def check_name(self, name: str = "test"):
        self.name_input.check_visible()
        self.name_input.check_have_value(name)

    def check_password(self, password: str = "pass"):
        self.password_input.check_visible()
        self.password_input.check_have_value(password)

    def check_checkboxes(self, checkboxes_name: list[str] | None = None):
        self.drink_checkbox_group.check_visible()
        if checkboxes_name is None:
            checkboxes_name = ["Water"]
        for name in checkboxes_name:
            self.drink_checkbox_group.check_checked(name)

    def check_radiobutton(self, radiobutton: str = "Red"):
        self.color_radiobutton_group.check_visible()
        self.color_radiobutton_group.check_selected(radiobutton)

    def check_selected_option(self, value: str = "yes"):
        self.automation_select.check_visible()
        self.automation_select.check_selected_value(value)

    def check_email(self, email: str = "test@test.com"):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

    def check_message(self, message: str = "Test message"):
        self.message_textarea.check_visible()
        self.message_textarea.check_have_value(message)
