import allure
import pytest

from pages.form_fields.forms_page import FormsPage
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.form_fields
@allure.tag(AllureTag.FORMS)
class TestFormFields:
    @allure.title("Test title and breadcrumbs at form fields")
    def test_popups_title_and_breadcrumbs(self, forms_page: FormsPage):
        forms_page.title_and_breadcrumbs.check_page_title()
        forms_page.title_and_breadcrumbs.check_home_link()
        forms_page.title_and_breadcrumbs.check_breadcrumbs_title()

    @allure.title("Test navigate from form fields to home")
    def test_navigate_from_form_field_to_home(self, forms_page: FormsPage):
        forms_page.title_and_breadcrumbs.click_home_link()
        forms_page.check_current_url("https://practice-automation.com/")

    @allure.title("Test click logo link")
    def test_form_fields_click_logo_link(self, forms_page: FormsPage):
        forms_page.navbar.click_logo_link()
        forms_page.navbar.check_current_url("https://practice-automation.com/")

    @allure.title("Test description at form fields")
    def test_popups_description(self, forms_page: FormsPage):
        forms_page.check_description()

    @allure.title("Test form at form fields")
    def test_form_fields_form(self, forms_page: FormsPage):
        forms_page.fill_name()
        forms_page.check_name()

        forms_page.fill_password()
        forms_page.check_password()

        forms_page.select_checkboxes()
        forms_page.check_checkboxes()

        forms_page.select_radiobutton()
        forms_page.check_radiobutton()

        forms_page.select_option()
        forms_page.check_selected_option()

        forms_page.check_automation_tools_label()
        forms_page.check_automation_tools()

        forms_page.fill_email()
        forms_page.check_email()

        forms_page.fill_message()
        forms_page.check_message()

    @allure.title("Test alert popup at form fields")
    def test_alert_popup(self, forms_page: FormsPage):
        forms_page.fill_name()
        forms_page.trigger_alert_form()

    @allure.title("Test copy from automation tools to message")
    def test_copy_from_automation_tools_to_message(self, forms_page: FormsPage):
        text = forms_page.get_automation_tools()
        forms_page.fill_message(text)
        forms_page.check_message(text)
