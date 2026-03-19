import allure
import pytest

from pages.popups.popups_page import PopupsPage
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.popups
@allure.tag(AllureTag.POPUPS)
class TestPopups:
    @allure.title("Test popups title and breadcrumbs")
    def test_popups_title_and_breadcrumbs(self, popups_page: PopupsPage):
        popups_page.check_title_and_breadcrumbs()

    @allure.title("Test popups description")
    def test_popups_description(self, popups_page: PopupsPage):
        popups_page.check_description()

    @allure.title("Test popups alert popup")
    def test_alert_popup(self, popups_page: PopupsPage):
        popups_page.trigger_alert_popup()

    @allure.title("Test popups confirm popup accept")
    def test_confirm_popup_accept(self, popups_page: PopupsPage):
        popups_page.trigger_confirm_popup_and_accept()

    @allure.title("Test popups confirm popup dismiss")
    def test_confirm_popup_dismiss(self, popups_page: PopupsPage):
        popups_page.trigger_confirm_popup_and_dismiss()

    @allure.title("Test popups prompt popup accept")
    @pytest.mark.parametrize("test_name", ["test", " ", "  ", "test#2", "test_#3", "test #4"])
    def test_prompt_popup_accept(self, popups_page: PopupsPage, test_name: str):
        popups_page.trigger_prompt_popup_accept(test_name)

    @allure.title("Test popups prompt popup dismiss")
    def test_prompt_popup_dismiss(self, popups_page: PopupsPage):
        popups_page.trigger_prompt_popup_dismiss()

    @allure.title("Test popups tooltip")
    def test_tooltip(self, popups_page: PopupsPage):
        popups_page.check_tooltip()
        popups_page.check_tooltip_result_not_visible()

        popups_page.click_tooltip()
        popups_page.check_tooltip_result()

        popups_page.click_tooltip_result()
        popups_page.check_tooltip_result_not_visible()
