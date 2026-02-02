import pytest

from Ui_auto.pages.LoginPage import LoginPage
from Ui_auto.pages.SignupPage import SignupPage

@pytest.mark.login
@pytest.mark.parametrize("email,password",[("rajvij8500@gmail.com","Vijay80741"),("rajvijvijayanegondi8500@gmail.com","Vijay80742")])
class TestLogin:
    def test_login(self,app_driver,email,password):
        register = SignupPage(app_driver)
        register.to_signup_page()
        login_check=LoginPage(app_driver)
        login_check.login_email(email)
        login_check.login_password(password)
        login_check.login()

    def test_smoke_user_login(self,app_driver,email,password):
        register = SignupPage(app_driver)
        register.to_signup_page()
        login_check = LoginPage(app_driver)
        login_check.user_login(email,password)