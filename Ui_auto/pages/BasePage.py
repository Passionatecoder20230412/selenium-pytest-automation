from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,app_driver):
        self.driver=app_driver
        self.wait=WebDriverWait(self.driver,10,ignored_exceptions=(NoSuchElementException,))

    def find_element(self,locator):
        self.driver.find_element(*locator)
    def button_click(self,locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()
        # self.driver.find_element(*locator).click()


    def verify_text(self, locator):
        abc=self.driver.find_element(*locator).text
        print(abc)
        return abc

    def enter_text(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)
    def select_normal(self,locator,target):
        select=Select(self.driver.find_element(*locator))
        for option in select.options:
            if option.text == target:
                option.click()
                break

    def select_by_visible_text(self,locator,text):
        ele=self.driver.find_element(*locator)
        Select(ele).select_by_visible_text(text)
    def select_by_index(self,locator,text):
        ele=self.driver.find_element(*locator)
        Select(ele).select_by_index(text)
    def select_by_value(self,locator,text):
        ele=self.driver.find_element(*locator)
        Select(ele).select_by_value(text)




