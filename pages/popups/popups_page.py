from components.footer.footer_component import FooterComponent
from components.navbar.navbar_component import NavbarComponent
from components.title_and_breadcrumbs.title_and_breadcrumbs_component import TitleAndBreadcrumbsComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage
from tools.locators.locator_strategy import LocatorStrategy


class PopupsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.title_and_breadcrumbs = TitleAndBreadcrumbsComponent(page, "Popups")
        self.description = Text(page, "p.wp-block-paragraph", "Popups description",
                                locator_strategy=LocatorStrategy.CSS)
        self.alert_popup_button = Button(page, "#alert", "Alert popup button",
                                         locator_strategy=LocatorStrategy.CSS)
        self.confirm_popup_button = Button(page, "#confirm", "Confirm popup button",
                                           locator_strategy=LocatorStrategy.CSS)
        self.confirm_popup_result = Text(page, "#confirmResult", "Confirm popup result",
                                         locator_strategy=LocatorStrategy.CSS)

        self.prompt_popup_button = Button(page, "#prompt", "Prompt popup button",
                                          locator_strategy=LocatorStrategy.CSS)
        self.prompt_popup_result = Text(page, "#promptResult", "Prompt popup result",
                                        locator_strategy=LocatorStrategy.CSS)

        self.tooltip_text = Text(page, ".tooltip_1", "Tooltip text",
                                 locator_strategy=LocatorStrategy.CSS)
        self.tooltip_result = Text(page, "#myTooltip", "Tooltip result",
                                   locator_strategy=LocatorStrategy.CSS)
        self.footer = FooterComponent(page)

    def check_title_and_breadcrumbs(self):
        self.title_and_breadcrumbs.check_breadcrumbs_title()
        self.title_and_breadcrumbs.check_page_title()
        self.title_and_breadcrumbs.check_home_link()

    def check_description(self):
        self.description.check_have_text("Popups (a.k.a., alerts) are a common feature in all modern web browsers. "
                                         "Use this page to practice handling the different type of popups that you "
                                         "may encounter. Click any of the buttons below to see a different popup.")

    def trigger_alert_popup(self):

        def handle_dialog(dialog):
            assert dialog.type == "alert"
            assert dialog.message == "Hi there, pal!"
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.alert_popup_button.click()

    def trigger_confirm_popup_and_accept(self):

        def handle_dialog(dialog):
            assert dialog.type == "confirm"
            assert dialog.message == "OK or Cancel, which will it be?"
            dialog.accept()
        self.page.once("dialog", handle_dialog)
        self.confirm_popup_button.click()

        self.confirm_popup_result.check_visible()
        self.confirm_popup_result.check_have_text("OK it is!")

    def trigger_confirm_popup_and_dismiss(self):

        def handle_dialog(dialog):
            assert dialog.type == "confirm"
            assert dialog.message == "OK or Cancel, which will it be?"
            dialog.dismiss()
        self.page.once("dialog", handle_dialog)
        self.confirm_popup_button.click()

        self.confirm_popup_result.check_visible()
        self.confirm_popup_result.check_have_text("Cancel it is!")

    def trigger_prompt_popup_accept(self, test_name: str):

        def handle_dialog(dialog):
            assert dialog.type == "prompt"
            assert dialog.message == "Hi there, what's your name?"
            dialog.accept(test_name)

        self.page.once("dialog", handle_dialog)
        self.prompt_popup_button.click()

        self.prompt_popup_result.check_visible()
        self.prompt_popup_result.check_have_text(f"Nice to meet you, {test_name}!")

    def trigger_prompt_popup_dismiss(self):

        def handle_dialog(dialog):
            assert dialog.type == "prompt"
            assert dialog.message == "Hi there, what's your name?"
            dialog.dismiss()

        self.page.once("dialog", handle_dialog)
        self.prompt_popup_button.click()

        self.prompt_popup_result.check_visible()
        self.prompt_popup_result.check_have_text(f"Fine, be that way...")

    def click_tooltip(self):
        self.tooltip_text.click()

    def click_tooltip_result(self):
        self.tooltip_result.click()

    def check_tooltip(self):
        self.tooltip_text.check_visible()
        self.tooltip_text.check_have_text("""<< click me to see a tooltip >>
              Cool text
            """)

    def check_tooltip_result(self):
        self.tooltip_result.check_visible()
        self.tooltip_result.check_have_text("Cool text")

    def check_tooltip_result_not_visible(self):
        self.tooltip_result.check_not_visible()
