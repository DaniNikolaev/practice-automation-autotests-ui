import allure
import pytest

from pages.main_page import MainPage


@pytest.mark.regression
@pytest.mark.main
class TestMain:
    @allure.title("Test navigation bar")
    def test_navbar(self, main_page: MainPage):
        main_page.navbar.check_navbar_is_visible()
        main_page.navbar.check_navbar_links()

    @allure.title("Test main title")
    def test_main_title(self, main_page: MainPage):
        main_page.check_title()

    @allure.title("Test main description")
    def test_main_description(self, main_page: MainPage):
        main_page.check_description()

    @allure.title("Test main buttons")
    def test_buttons(self, main_page: MainPage):
        main_page.check_forms_button()
        main_page.check_events_button()
        main_page.check_popups_button()
        main_page.check_slider_button()

    @allure.title("Test footer")
    def test_footer(self, main_page: MainPage):
        main_page.footer.check_footer_visible()
        main_page.footer.check_footer_text()
        main_page.footer.check_footer_links()
