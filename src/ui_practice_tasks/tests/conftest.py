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
def web_tables_page(page, home_page):
    def _create(mode="default"):
        if mode == "use_base_url":
            return home_page.open_web_tables_page()

        elif mode == "use_table_url":
            page.goto(BASE_URL + "/webtables")
            return WebTablesPages(page)

        # default behavior
        page.goto(BASE_URL + "/webtables")
        return WebTablesPages(page)

    return _create


# @pytest.fixture
# def web_tables_page(page, home_page, request):
#     # Read raw parametrization value for 'base_url' if present.
#     param = None
#     #callspec = getattr(getattr(request, "node", None), "callspec", None)
    
#     if hasattr(request, "node") and hasattr(request.node, "callspec"):
#         callspec = request.node.callspec
#     else:
#         callspec = None

#     page.pause()
#     if callspec:
#         param = callspec.params.get("base_url")

#     if param == "use_base_url":
#         return home_page.open_web_tables_page()
#     if param == "use_table_url":
#         page.goto(BASE_URL + "/webtables")
#         return WebTablesPages(page)

#     # Default behaviour: navigate directly to the webtables URL.
#     page.goto(BASE_URL + "/webtables")
#     return WebTablesPages(page)


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



