from selenium import webdriver
import pytest

BASE_URL="https://automationexercise.com/"
# @pytest.fixture(params=["chrome","edge","firefox"])
@pytest.fixture
def app_driver():

    # if request.param == "chrome":
    print("**********---------setup---------*****************")
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(50)
    yield driver
    # elif request.param == "edge":
    #     print("**********---------setup---------*****************")
    #     driver = webdriver.Edge()
    #     driver.maximize_window()
    #     driver.get(BASE_URL)
    #     yield driver
    # else:
    #     print("**********---------setup---------*****************")
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.get(BASE_URL)
    #     yield driver

    print("**********---------teardown---------***************")
    driver.quit()

