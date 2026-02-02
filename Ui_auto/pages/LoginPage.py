from selenium.webdriver.common.by import By

from Ui_auto.pages.BasePage import BasePage


class LoginPage(BasePage):
    SIGNUP_PAGE = (By.CSS_SELECTOR, '[href="/login"]')
    LOGIN_EMAIL=(By.CSS_SELECTOR,'[data-qa="login-email"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    LOGIN=(By.CSS_SELECTOR,'[data-qa="login-button"]')
    def __init__(self,driver):
        super().__init__(driver)
    def login_navigate(self):
        self.button_click(self.SIGNUP_PAGE)
    def login_email(self,text):
        self.enter_text(self.LOGIN_EMAIL,text)
    def login_password(self,text):
        self.enter_text(self.LOGIN_PASSWORD,text)
    def login(self):
        self.button_click(self.LOGIN)
    def user_login(self,email,password):
        self.button_click(self.SIGNUP_PAGE)
        self.enter_text(self.LOGIN_EMAIL, email)
        self.enter_text(self.LOGIN_PASSWORD, password)
        self.button_click(self.LOGIN)




