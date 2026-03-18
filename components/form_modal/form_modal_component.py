from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.submission_summary.submission_summary_component import SubmissionSummaryComponent
from elements.button import Button
from elements.input import Input
from elements.link import Link
from elements.text import Text
from elements.textarea import Textarea
from tools.locators.locator_strategy import LocatorStrategy


class FormModalComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "#pum_popup_title_674", "Form Modal title",
                          locator_strategy=LocatorStrategy.CSS)
        self.close_button = Button(page, "#popmake-674 button.pum-close.popmake-close", "Form Modal close button",
                                   locator_strategy=LocatorStrategy.CSS)
        self.description = Text(page, "#popmake-674 strong", "Form Modal description",
                                locator_strategy=LocatorStrategy.CSS)
        self.back_link = Link(page, "[data-wp-on--click='actions.goBack']", "Form Modal back button",
                              locator_strategy=LocatorStrategy.CSS)
        self.form_title = Text(page, "#contact-form-success-header-99ddf6d0cf76daf0c77607b1cc134112e4314c10",
                               "Form Modal form title",
                               locator_strategy=LocatorStrategy.CSS)
        self.name_label = Text(page, "label.grunion-field-label.name", "Form Modal name label",
                               locator_strategy=LocatorStrategy.CSS)
        self.name_input = Input(page, "#g1051-name", "Form Modal name input",
                                locator_strategy=LocatorStrategy.CSS)
        self.name_required_label = Text(page, "#g1051-name-text-error-message", "Form Modal name required label",
                                        locator_strategy=LocatorStrategy.CSS)
        self.email_label = Text(page, "label.grunion-field-label.email", "Form Modal email label",
                                locator_strategy=LocatorStrategy.CSS)
        self.email_input = Input(page, "#g1051-email", "Form Modal email input",
                                 locator_strategy=LocatorStrategy.CSS)
        self.message_label = Text(page, "label.grunion-field-label.textarea", "Form Modal message label",
                                  locator_strategy=LocatorStrategy.CSS)
        self.message_textarea = Textarea(page, "#contact-form-comment-g1051-message", "Form Modal message textarea",
                                         locator_strategy=LocatorStrategy.CSS)
        self.after_form_label = Text(page, "span.contact-form__error-message", "Form Modal after form label",
                                     locator_strategy=LocatorStrategy.CSS)
        self.submit_button = Button(page, "Submit", "Form Modal submit button",
                                    locator_strategy=LocatorStrategy.TEXT)

        self.submission_summary = SubmissionSummaryComponent(page)

    def check_title(self):
        self.title.check_visible()
        self.title.check_have_text("Modal Containing A Form")

    def check_title_not_visible(self):
        self.title.check_not_visible()

    def check_close_button(self):
        self.close_button.check_visible()
        self.close_button.check_enabled()

    def check_close_button_not_visible(self):
        self.close_button.check_not_visible()

    def click_close_button(self):
        self.close_button.click()

    def check_description(self):
        self.description.check_visible()
        self.description.check_have_text("Please enter your contact info below.")

    def check_description_not_visible(self):
        self.description.check_not_visible()

    def check_back_link(self):
        self.back_link.check_visible()
        self.back_link.check_have_attribute("href", "/modals/")

    def check_back_link_not_visible(self):
        self.back_link.check_not_visible()

    def click_back_link(self):
        self.back_link.click()

    def check_form_title(self):
        self.form_title.check_visible()
        self.form_title.check_have_text("Thank you for your response.")

    def check_form_title_not_visible(self):
        self.form_title.check_not_visible()

    def check_form(self, name: str = "Name", email: str = "test@test.com", message: str = "Message"):
        self.name_label.check_visible()
        self.name_label.check_have_text("Name(required)")
        self.name_input.check_have_value(name)

        self.email_label.check_visible()
        self.email_label.check_have_text("Email")
        self.email_input.check_have_value(email)

        self.message_label.check_visible()
        self.message_label.check_have_text("Message")
        self.message_textarea.check_have_value(message)

    def check_form_not_visible(self):
        self.name_label.check_not_visible()
        self.name_input.check_not_visible()
        self.email_label.check_not_visible()
        self.email_input.check_not_visible()
        self.message_label.check_not_visible()
        self.message_textarea.check_not_visible()

    def fill_form(self, name: str = "Name", email: str = "test@test.com", message: str = "Message"):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.message_textarea.fill(message)

    def check_name_required(self):
        self.name_required_label.check_visible()
        self.name_required_label.check_have_text("This field is required.")

    def check_name_required_not_visible(self):
        self.name_required_label.check_not_visible()

    def check_after_form(self):
        self.after_form_label.check_visible()
        self.after_form_label.check_have_text("Please fill out the form correctly.")

    def check_after_form_not_visible(self):
        self.after_form_label.check_not_visible()

    def check_submit_button(self):
        self.submit_button.check_visible()
        self.submit_button.check_enabled()

    def check_submit_button_not_visible(self):
        self.submit_button.check_not_visible()

    def click_submit_button(self):
        self.submit_button.click()
