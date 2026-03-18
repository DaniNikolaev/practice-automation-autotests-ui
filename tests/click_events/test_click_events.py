import allure
import pytest

from pages.click_events.events_page import EventsPage


@pytest.mark.regression
@pytest.mark.click_events
class TestClickEvents:
    @allure.title("Test click events title and breadcrumbs")
    def test_click_events_title_and_breadcrumbs(self, events_page: EventsPage):
        events_page.check_title_and_breadcrumbs()

    @allure.title("Test click events description")
    def test_click_events_description(self, events_page: EventsPage):
        events_page.check_description()

    @allure.title("Test click animals button")
    @pytest.mark.parametrize("animal_name", ["Cat", "Dog", "Pig", "Cow"])
    def test_click_animals_button(self, events_page: EventsPage, animal_name: str):
        events_page.click_animal_button(animal_name)
        events_page.check_result_text(animal_name)
