import allure

from components.base_component import BaseComponent
from elements.text import Text
from elements.base_element import LocatorStrategy


class SubmissionSummaryComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.name_field = Text(
            page,
            "[data-wp-text='context.submission.value'] >> nth=0",
            "Name field value",
            locator_strategy=LocatorStrategy.CSS
        )

        self.email_field = Text(
            page,
            "[data-wp-text='context.submission.value'] >> nth=2",
            "Email field value",
            locator_strategy=LocatorStrategy.CSS
        )

        self.message_field = Text(
            page,
            "[data-wp-text='context.submission.value'] >> nth=4",
            "Message field value",
            locator_strategy=LocatorStrategy.CSS
        )

        self.name_label = Text(
            page,
            "[data-wp-text='context.submission.label'] >> nth=0",
            "Name label",
            locator_strategy=LocatorStrategy.CSS
        )

        self.email_label = Text(
            page,
            "[data-wp-text='context.submission.label'] >> nth=1",
            "Email label",
            locator_strategy=LocatorStrategy.CSS
        )

        self.message_label = Text(
            page,
            "[data-wp-text='context.submission.label'] >> nth=2",
            "Message label",
            locator_strategy=LocatorStrategy.CSS
        )

    @allure.step("Check submission summary form")
    def check_submission(self, name: str = "Name", email: str = "test@test.com", message: str = "Message"):
        self.name_label.check_visible()
        self.name_label.check_have_text("Name:")
        self.name_field.check_have_text(name)

        self.email_label.check_visible()
        self.email_label.check_have_text("Email:")
        self.email_field.check_have_text(email)

        self.email_label.check_visible()
        self.message_label.check_have_text("Message:")
        self.message_field.check_have_text(message)
