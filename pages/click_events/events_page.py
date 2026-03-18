from components.footer.footer_component import FooterComponent
from components.navbar.navbar_component import NavbarComponent
from components.title_and_breadcrumbs.title_and_breadcrumbs_component import TitleAndBreadcrumbsComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage
from tools.locators.locator_strategy import LocatorStrategy


class EventsPage(BasePage):
    ANIMALS = {"Cat": "Meow!", "Dog": "Woof!", "Pig": "Oink!", "Cow": "Moo!"}

    def __init__(self, page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.title_and_breadcrumbs = TitleAndBreadcrumbsComponent(page, "Click Events")
        self.description = Text(page, "p.wp-block-paragraph", "Description",
                                locator_strategy=LocatorStrategy.CSS)
        self.animal_buttons = {animal: Button(page,
                                              animal,
                                              f"{animal} button",
                                              locator_strategy=LocatorStrategy.TEXT
                                              )
                               for animal in self.ANIMALS.keys()
                               }

        self.result_text = Text(page, "#demo", "Result text",
                                locator_strategy=LocatorStrategy.CSS)

        self.footer = FooterComponent(page)

    def check_title_and_breadcrumbs(self):
        self.title_and_breadcrumbs.check_breadcrumbs_title()
        self.title_and_breadcrumbs.check_page_title()
        self.title_and_breadcrumbs.check_home_link()

    def check_description(self):
        self.description.check_have_text("Click any of the buttons below to see some text. Then, you can write an "
                                         "automated test that clicks any of the buttons and asserts that the expected"
                                         " text is present on the screen.")

    def click_animal_button(self, animal_name: str):
        self.animal_buttons[animal_name].click()

    def check_result_text(self, animal_name: str):
        self.result_text.check_have_text(self.ANIMALS[animal_name])
