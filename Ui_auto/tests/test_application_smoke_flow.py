import time

import pytest

from Ui_auto.pages.LoginPage import LoginPage
from Ui_auto.pages.ProductsPage import ProductsPage
from Ui_auto.pages.SignupPage import SignupPage
from Ui_auto.tests.test_add_products import TestAddProduct
from Ui_auto.tests.test_login import TestLogin
from Ui_auto.tests.test_signup_page import TestSignup

@pytest.mark.critical
@pytest.mark.parametrize("name,email,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobile_number",[("vijay",f"rajvijay85248593553{time.time()}@gmail.com","Vijay80741","20","August",
                                                                      22,"Vijay","Anegondi","DXC fraud company","Thadigadapa","Vijayawada","India","Andhra","Vijayawada","516216","9490859263")])
class TestCritical:
    def test_critical(self,app_driver,name,email,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobile_number):
        self.driver=app_driver
        self.driver.implicitly_wait(30)
        register = SignupPage(app_driver)
        register.to_signup_page()
        # ab=self.driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/h2')
        # print(ab.text)
        # assert ab.text =="New User Signup!"

        register.enter_signup_name(name)
        # register.enter_signup_email(f"rajvijay{time.time()}@gmail.com")
        register.enter_signup_email(email)
        register.signup_button_click()
        register.title_radio()
        register.password(password)
        register.days(day)
        register.months(month)
        register.years(year)
        register.newsletter_check()
        register.offers_from_partners()
        register.firstname(firstname)
        register.lastname(lastname)
        register.company(company)
        register.address(address)
        register.address2(address2)
        register.country(country)
        register.state(state)
        register.city(city)
        register.zipcode(zipcode)
        register.mobile_number(mobile_number)
        register.create_account()
        print("----------account created successfully----------")
        self.driver.refresh()
        # register = SignupPage(app_driver)
        # register.to_signup_page()
        # login_check = LoginPage(app_driver)
        # login_check.user_login(email, password)
        # print("login successful")
        add_products = ProductsPage(app_driver)

        add_products.navigate_products()
        # driver.find_element(By.CSS_SELECTOR, '[data-product-id="2"]').click()
        time.sleep(10)
        add_products.add_product()
        print("------------added products successful---------------")

