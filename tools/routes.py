from enum import Enum


class AppRoute(str, Enum):
    MAIN = "./"
    FORMS = "./form-fields"
    EVENTS = "./click-events"
    POPUPS = "./popups"
    SLIDER = "./slider"
    MODALS = "./modals"
