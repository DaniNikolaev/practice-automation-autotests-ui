import allure
import pytest

from pages.slider_page.slider_page import SliderPage
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.slider
@allure.tag(AllureTag.SLIDER)
class TestSlider:
    @allure.title("Test slider title and breadcrumbs")
    def test_slider_title_and_breadcrumbs(self, slider_page: SliderPage):
        slider_page.check_title_and_breadcrumbs()

    @allure.title("Test slider description")
    def test_slider_description(self, slider_page: SliderPage):
        slider_page.check_description()

    @allure.title("Test slider value")
    @pytest.mark.parametrize("value", [0, 10, 20, 40, 60, 80, 100])
    def test_slider_value(self, slider_page: SliderPage, value: int):
        slider_page.check_slider_value()

        slider_page.move_slider(value)
        slider_page.slider_value.check_visible()
        slider_page.slider_value.check_have_text(str(value))
