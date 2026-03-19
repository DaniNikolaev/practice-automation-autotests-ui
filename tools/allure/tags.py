from enum import Enum


class AllureTag(str, Enum):
    FORMS = "FORMS"
    EVENTS = "EVENTS"
    POPUPS = "POPUPS"
    SLIDER = "SLIDER"
    MODALS = "MODALS"
    MAIN = "MAIN"
