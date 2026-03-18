import allure
import pytest

from pages.modals.modals_page import ModalsPage


@pytest.mark.regression
@pytest.mark.modals
class TestModals:
    @allure.title("Test modals title and breadcrumbs")
    def test_modals_title_and_breadcrumbs(self, modals_page: ModalsPage):
        modals_page.check_title_and_breadcrumbs()

    @allure.title("Test modals description")
    def test_modals_description(self, modals_page: ModalsPage):
        modals_page.check_description()

    @allure.title("Test simple modal")
    def test_simple_modal(self, modals_page: ModalsPage):
        modals_page.check_simple_modal_label()
        modals_page.check_simple_modal_button()

        modals_page.click_simple_modal_button()
        modals_page.check_simple_modal()

        modals_page.simple_modal.click_close_button()
        modals_page.check_simple_modal_not_visible()

    @allure.title("Test form modal")
    def test_form_modal(self, modals_page: ModalsPage):
        modals_page.check_form_modal_label()
        modals_page.check_form_modal_button()

        modals_page.click_form_modal_button()

        modals_page.form_modal.name_label.click()
        modals_page.form_modal.name_label.click()
        modals_page.form_modal.check_name_required()

        modals_page.form_modal.fill_form()
        modals_page.check_form_modal()
        modals_page.form_modal.click_submit_button()

        modals_page.form_modal.submission_summary.check_submission()

        modals_page.form_modal.click_close_button()
        modals_page.check_form_modal_not_visible()
