import allure
import pytest

from pages.form_fields.forms_page import FormsPage


@pytest.mark.regression
@pytest.mark.form_fields
class TestFormFields:
    @allure.title("Test title and breadcrumbs at form fields")
    def test_popups_title_and_breadcrumbs(self, forms_page: FormsPage):
        forms_page.title_and_breadcrumbs.check_page_title()
        forms_page.title_and_breadcrumbs.check_home_link()
        forms_page.title_and_breadcrumbs.check_breadcrumbs_title()

    @allure.title("Test description at form fields")
    def test_popups_description(self, forms_page: FormsPage):
        forms_page.check_description()

    @allure.title("Test form at form fields")
    def test_form_fields(self, forms_page: FormsPage):
        forms_page.fill_name()
        forms_page.check_name()

        forms_page.fill_password()
        forms_page.check_password()

        forms_page.fill_email()
        forms_page.check_email()

        forms_page.fill_message()
        forms_page.check_password()

        forms_page.select_checkboxes()
        forms_page.check_checkboxes()

        forms_page.select_radiobutton()
        forms_page.check_radiobutton()

        forms_page.select_option()
        forms_page.check_selected_option()
