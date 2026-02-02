import random
import time

from selenium.webdriver.common.by import By

from Ui_auto.pages.BasePage import BasePage


class ProductsPage(BasePage):
    PRODUCTS_LINK=(By.CSS_SELECTOR,'[href="/products"]')
    # ADD_PRODUCT_ID=(By.CSS_SELECTOR,f'[data-product-id="{random."]')
    CONTINUE_SHOPPING=(By.CSS_SELECTOR,f'[class="btn btn-success close-modal btn-block"]')
    def __init__(self,driver):
        super().__init__(driver)
    def navigate_products(self):
        self.button_click(self.PRODUCTS_LINK)
        time.sleep(2)
    def add_product(self):
        product_id=random.randint(1,5)
        ADD_PRODUCT_ID=(By.CSS_SELECTOR,f'[data-product-id="{product_id}"]')
        for i in range(5):
            self.button_click(ADD_PRODUCT_ID)
            time.sleep(0.3)
            self.button_click(self.CONTINUE_SHOPPING)
    def smoke_add_products(self):
        time.sleep(2)
        self.button_click(self.PRODUCTS_LINK)
        product_id = random.randint(1, 5)
        ADD_PRODUCT_ID = (By.CSS_SELECTOR, f'[data-product-id="{product_id}"]')
        for i in range(5):
            self.button_click(ADD_PRODUCT_ID)
            time.sleep(0.3)
            self.button_click(self.CONTINUE_SHOPPING)





