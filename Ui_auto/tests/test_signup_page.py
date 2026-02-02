import time

import pytest
from selenium.webdriver.common.by import By

from Ui_auto.pages.SignupPage import SignupPage


@pytest.mark.register
@pytest.mark.parametrize("name,email,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobile_number",[("vijay",f"rajvij8500{time.time()}@gmail.com","Vijay80741","20","August",
                                                                      22,"Vijay","Anegondi","DXC fraud company","Thadigadapa","Vijayawada","India","Andhra","Vijayawada","516216","9490859263")])
class TestSignup:

    # def test_signup_page(self,app_driver):
    def test_signup_page(self,app_driver,name,email,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobile_number):
        # self.driver=app_driver
        register=SignupPage(app_driver)
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




