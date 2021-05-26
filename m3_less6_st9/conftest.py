import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language for the loading page")


@pytest.fixture(scope="function")
def browser(request):
    page_lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': page_lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit