import pytest
from selene import browser


@pytest.fixture(scope="session")
def open_browser(request):
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open("https://google.com/ncr")

    yield

    browser.quit()
