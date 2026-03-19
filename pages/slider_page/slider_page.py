import allure
from playwright.sync_api import Page

from components.footer.footer_component import FooterComponent
from components.navbar.navbar_component import NavbarComponent
from components.title_and_breadcrumbs.title_and_breadcrumbs_component import TitleAndBreadcrumbsComponent
from elements.slider import Slider
from elements.text import Text
from pages.base_page import BasePage
from tools.locators.locator_strategy import LocatorStrategy


class SliderPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.title_and_breadcrumbs = TitleAndBreadcrumbsComponent(page, "Slider")
        self.description = Text(page, "p.wp-block-paragraph", "Slider description",
                                locator_strategy=LocatorStrategy.CSS)
        self.slider = Slider(page, "#slideMe", "Slider slider",
                             locator_strategy=LocatorStrategy.CSS)
        self.slider_value = Text(page, "#value", "Slider value",
                                 locator_strategy=LocatorStrategy.CSS)

        self.footer = FooterComponent(page)

    @allure.step("Check slider title and breadcrumbs")
    def check_title_and_breadcrumbs(self):
        self.title_and_breadcrumbs.check_breadcrumbs_title()
        self.title_and_breadcrumbs.check_page_title()
        self.title_and_breadcrumbs.check_home_link()

    def check_description(self):
        self.description.check_visible()
        self.description.check_have_text("This is a range slider. You can adjust it by clicking a given area of the "
                                         "element (easier) or by using a drag-and-drop operation (harder). As you "
                                         "move the slider, the current value will be updated.")

    def move_slider(self, value: int):
        self.slider.set_value(value)

    def check_slider_value(self, value: int = 25):
        self.slider.check_value(value)
