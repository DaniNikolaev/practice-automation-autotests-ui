import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config import settings
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(params=settings.browsers)
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)
