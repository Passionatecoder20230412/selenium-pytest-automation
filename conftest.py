# from selenium import webdriver
# import pytest
#
# BASE_URL="https://automationexercise.com/"
# # @pytest.fixture(params=["chrome","edge","firefox"])
# @pytest.fixture
# def app_driver():
#
#     # if request.param == "chrome":
#     print("**********---------setup---------*****************")
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(BASE_URL)
#     driver.implicitly_wait(50)
#     yield driver
#     # elif request.param == "edge":
#     #     print("**********---------setup---------*****************")
#     #     driver = webdriver.Edge()
#     #     driver.maximize_window()
#     #     driver.get(BASE_URL)
#     #     yield driver
#     # else:
#     #     print("**********---------setup---------*****************")
#     #     driver = webdriver.Firefox()
#     #     driver.maximize_window()
#     #     driver.get(BASE_URL)
#     #     yield driver
#
#     print("**********---------teardown---------***************")
#     driver.quit

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from config.config import Config


# ---------------- session setup ----------------
def pytest_sessionstart(session):
    Config.setup_directories()


# ---------------- CLI options ----------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=Config.BROWSER,
        help="Browser: chrome"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run in headless mode (for Jenkins)"
    )


# ---------------- driver fixture ----------------
@pytest.fixture(scope="function")
def app_driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)

    yield driver

    driver.quit()
