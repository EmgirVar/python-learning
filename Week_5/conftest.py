import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    page.screenshot(path="screenshot.png")
    context.close()

@pytest.fixture
def login_page(page):
    page.goto("https://www.saucedemo.com/")
    return page

@pytest.fixture
def inventory_page(page):
    page.goto("https://www.saucedemo.com/inventory.html/")
    return page

