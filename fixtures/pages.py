import pytest
from playwright.sync_api import Page

from pages.click_events.events_page import EventsPage
from pages.form_fields.forms_page import FormsPage
from pages.main_page import MainPage
from pages.modals.modals_page import ModalsPage
from pages.popups.popups_page import PopupsPage
from pages.slider_page.slider_page import SliderPage
from tools.routes import AppRoute


@pytest.fixture()
def main_page(chromium_page: Page) -> MainPage:
    p = MainPage(page=chromium_page)
    p.visit(AppRoute.MAIN)
    return p


@pytest.fixture()
def forms_page(chromium_page: Page) -> FormsPage:
    p = FormsPage(page=chromium_page)
    p.visit(AppRoute.FORMS)
    return p


@pytest.fixture()
def events_page(chromium_page: Page) -> EventsPage:
    p = EventsPage(page=chromium_page)
    p.visit(AppRoute.EVENTS)
    return p


@pytest.fixture()
def popups_page(chromium_page: Page) -> PopupsPage:
    p = PopupsPage(page=chromium_page)
    p.visit(AppRoute.POPUPS)
    return p


@pytest.fixture()
def slider_page(chromium_page: Page) -> SliderPage:
    p = SliderPage(page=chromium_page)
    p.visit(AppRoute.SLIDER)
    return p


@pytest.fixture()
def modals_page(chromium_page: Page) -> ModalsPage:
    p = ModalsPage(page=chromium_page)
    p.visit(AppRoute.MODALS)
    return p
