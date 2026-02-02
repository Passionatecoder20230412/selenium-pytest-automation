import time

import pytest
from selenium.webdriver.common.by import By

from Ui_auto.pages.ProductsPage import ProductsPage
@pytest.mark.smoke
@pytest.mark.add_product
class TestAddProduct:
    def test_add_product(self,app_driver):
        driver=app_driver
        add_products=ProductsPage(app_driver)

        add_products.navigate_products()
        # driver.find_element(By.CSS_SELECTOR, '[data-product-id="2"]').click()
        time.sleep(10)
        add_products.add_product()
        print("------------444444444444444---------------")