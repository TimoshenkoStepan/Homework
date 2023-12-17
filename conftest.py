import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Enter the ISO 639-1 language code")

@pytest.fixture(scope="function")
def browser():
    #Returns chrome browser
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def language(request):
    #Returns the ISO 639-1 language code
    language_code = str(request.config.getoption("language"))
    #Check that the language_code is two letters
    if language_code.isalpha() and len(language_code) == 2:
        return language_code
    else:
        raise pytest.UsageError("--language should be the ISO 639-1 language code")

