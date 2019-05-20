from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")
    MY_NAME = "VolodymyrStepanov"
    MY_PASS = "VolodymyrStepanov"
    TEST_URL = "http://jira.hillel.it/secure/Dashboard.jspa"
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def login_to_jira(self, username=MY_NAME, password=MY_PASS):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.driver.title

    def login_form_presented(self):
        return WebDriverWait(self.driver, 5)\
            .until(ec.presence_of_element_located((By.ID, "login-form-username")))

    def auth_failed(self):
        return WebDriverWait(self.driver, 5)\
            .until(ec.presence_of_element_located((By.ID, "usernameerror")))

    def open(self):
        self.driver.get(self.TEST_URL)
        return self

