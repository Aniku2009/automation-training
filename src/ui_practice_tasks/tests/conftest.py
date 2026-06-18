import pytest
from playwright.sync_api import sync_playwright

from ui_practice_tasks.pages.home_page import HomePage
from ui_practice_tasks.pages.home_page import WebTablesPages
from ui_practice_tasks.pages.home_page import ButtonsPages
from ui_practice_tasks.pages.home_page import TextBoxPages
from ui_practice_tasks.pages.home_page import CheckBoxPages
from ui_practice_tasks.pages.home_page import PracticeFormPages
from ui_practice_tasks.pages.home_page import RadioButtonPages

BASE_URL = "https://demoqa.com"

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page

        browser.close()


@pytest.fixture
def home_page(page):
    page.goto(BASE_URL)
    return HomePage(page)


@pytest.fixture
def web_tables_page(page):
    #page.pause()
    page.goto(BASE_URL +  "/webtables")
    return WebTablesPages(page)


@pytest.fixture
def buttons_page(page):
    page.goto(BASE_URL +  "/buttons")
    return ButtonsPages(page)

@pytest.fixture
def check_box_page(page):
    page.goto(BASE_URL +  "/checkbox")
    return CheckBoxPages(page)

@pytest.fixture
def practice_form_page(page):
    page.goto(BASE_URL +  "/automation-practice-form")
    return PracticeFormPages(page)

@pytest.fixture
def radio_button_page(page):
    page.goto(BASE_URL +  "/radio-button")
    return RadioButtonPages(page)

@pytest.fixture
def text_box_page(page):
    page.goto(BASE_URL +  "/text-box")
    return TextBoxPages(page)



