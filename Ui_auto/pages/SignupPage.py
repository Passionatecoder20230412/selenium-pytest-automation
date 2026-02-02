from selenium.webdriver.common.by import By

from Ui_auto.pages.BasePage import BasePage

class SignupPage(BasePage):
    """
    locators
    actions
    """
    #locators
    SIGNUP_PAGE = (By.CSS_SELECTOR,'[href="/login"]')
    SIGNUP_PAGE_NAME_VERIFY=(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/h2')
    SIGNUP_NAME = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGNUP_EMAIL = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_PART1 = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
    TITLE=(By.CSS_SELECTOR,'[id="id_gender1"]')
    PASSWORD = (By.CSS_SELECTOR, '[type="password"]')
    DAYS = (By.CSS_SELECTOR, '[data-qa="days"]')
    MONTHS = (By.CSS_SELECTOR, '[data-qa="months"]')
    YEARS = (By.CSS_SELECTOR, '[data-qa="years"]')
    CHECKBOX_NEWSLETTER = (By.CSS_SELECTOR, '[id="newsletter"]')
    OFFERS_FROM_PARTNERS= (By.CSS_SELECTOR, '[name="optin"]')
    FIRST_NAME = (By.CSS_SELECTOR, '[data-qa="first_name"]')
    LAST_NAME = (By.CSS_SELECTOR, '[data-qa="last_name"]')
    COMPANY = (By.CSS_SELECTOR, '[data-qa="company"]')
    ADDRESS= (By.CSS_SELECTOR, '[data-qa="address"]')
    ADDRESS2= (By.CSS_SELECTOR, '[data-qa="address2"]')
    COUNTRY = (By.CSS_SELECTOR, '[data-qa="country"]')
    STATE = (By.CSS_SELECTOR, '[data-qa="state"]')
    CITY = (By.CSS_SELECTOR, '[data-qa="city"]')
    ZIPCODE = (By.CSS_SELECTOR, '[data-qa="zipcode"]')
    MOBILE_NUMBER = (By.CSS_SELECTOR, '[data-qa="mobile_number"]')
    CREATE_ACCOUNT= (By.CSS_SELECTOR, '[data-qa="create-account"]')

    def __init__(self,driver):
        super().__init__(driver)

    def to_signup_page(self):
        self.button_click(self.SIGNUP_PAGE)
    def signup_page_name_verify(self):
        self.verify_text(self.SIGNUP_PAGE_NAME_VERIFY)
    def enter_signup_name(self,text):
        self.enter_text(self.SIGNUP_NAME,text)
    def enter_signup_email(self,text):
        self.enter_text(self.SIGNUP_EMAIL,text)
    def signup_button_click(self):
        self.button_click(self.SIGNUP_PART1)
    def title_radio(self):
        self.button_click(self.TITLE)
    def password(self,text):
        self.enter_text(self.PASSWORD,text)
    def days(self,text):
        self.select_by_value(self.DAYS,text)
    def months(self,text):
        self.select_by_visible_text(self.MONTHS,text)
    def years(self,text):
        self.select_by_index(self.YEARS,text)
    def newsletter_check(self):
        self.button_click(self.CHECKBOX_NEWSLETTER)
    def offers_from_partners(self):
        self.button_click(self.OFFERS_FROM_PARTNERS)
    def firstname(self,text):
        self.enter_text(self.FIRST_NAME,text)
    def lastname(self,text):
        self.enter_text(self.LAST_NAME,text)
    def company(self,text):
        self.enter_text(self.COMPANY,text)
    def address(self,text):
        self.enter_text(self.ADDRESS,text)
    def address2(self,text):
        self.enter_text(self.ADDRESS2,text)
    def country(self,target):
        self.select_normal(self.COUNTRY,target)
    def state(self,text):
        self.enter_text(self.STATE,text)
    def city(self,text):
        self.enter_text(self.CITY,text)
    def zipcode(self,text):
        self.enter_text(self.ZIPCODE,text)
    def mobile_number(self,text):
        self.enter_text(self.MOBILE_NUMBER,text)
    def create_account(self):
        self.button_click(self.CREATE_ACCOUNT)

    def signup_new_user_from_testdata(
            self, name, email, password, day, month, year,
            firstname, lastname, company, address, address2,
            country, state, city, zipcode, mobile_number):
        self.to_signup_page()
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.signup_button_click()

        self.title_radio()
        self.password(password)
        self.days(day)
        self.months(month)
        self.years(year)

        self.newsletter_check()
        self.offers_from_partners()
        self.firstname(firstname)
        self.lastname(lastname)
        self.company(company)
        self.address(address)
        self.address2(address2)

        self.country(country)
        self.state(state)
        self.city(city)
        self.zipcode(zipcode)
        self.mobile_number(mobile_number)

        self.create_account()






