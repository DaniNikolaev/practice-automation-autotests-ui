from enum import Enum


class LocatorStrategy(str, Enum):
    TEST_ID = "test_id"
    CSS = "css"
    XPATH = "xpath"
    TEXT = "text"
    ROLE = "role"
    LABEL = "label"
    PLACEHOLDER = "placeholder"
    ALT_TEXT = "alt_text"
    TITLE = "title"
