import allure
import pytest

from pages.main.main_page import MainPage
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.main
@allure.tag(AllureTag.MAIN)
class TestMain:
    @allure.title("Test navigation bar")
    def test_navbar(self, main_page: MainPage):
        main_page.navbar.check_navbar_is_visible()
        main_page.navbar.check_navbar_links()

    @allure.title("Test click logo")
    def test_click_logo(self, main_page: MainPage):
        main_page.navbar.click_logo_link()
        main_page.check_current_url("https://practice-automation.com/")

    @allure.title("Test click Courses")
    def test_click_courses(self, main_page: MainPage):
        main_page.navbar.click_courses_link()
        main_page.check_current_url("https://automatenow-courses.teachable.com/")

    @allure.title("Test click Blog")
    def test_click_blog(self, main_page: MainPage):
        main_page.navbar.click_blog_link()
        main_page.check_current_url("https://automatenow.io/")

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

    @allure.title("Test navigate to form fields")
    def test_navigate_to_form_fields(self, main_page: MainPage):
        main_page.click_forms_button()
        main_page.check_current_url("https://practice-automation.com/form-fields/")

    @allure.title("Test navigate to click events")
    def test_navigate_to_click_events(self, main_page: MainPage):
        main_page.click_events_button()
        main_page.check_current_url("https://practice-automation.com/click-events/")

    @allure.title("Test navigate to popups")
    def test_navigate_to_popups(self, main_page: MainPage):
        main_page.click_popups_button()
        main_page.check_current_url("https://practice-automation.com/popups/")

    @allure.title("Test navigate to modals")
    def test_navigate_to_modals(self, main_page: MainPage):
        main_page.click_modals_button()
        main_page.check_current_url("https://practice-automation.com/modals/")

    @allure.title("Test navigate to slider")
    def test_navigate_to_modals(self, main_page: MainPage):
        main_page.click_slider_button()
        main_page.check_current_url("https://practice-automation.com/slider/")

    @allure.title("Test footer")
    def test_footer(self, main_page: MainPage):
        main_page.footer.check_footer_visible()
        main_page.footer.check_footer_text()
        main_page.footer.check_footer_links()
