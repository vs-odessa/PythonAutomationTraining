from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestJira:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    def test_login_to_jira(self):
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # login_page = LoginPage(driver)
        self.login_page.open()
        # driver.get("https://jira.hillel.it/secure/Dashboard.jspa")
        # assert "System Dashboard - Hillel IT School JIRA" in driver.title
        assert self.login_page.at_page()

        # profile_logo_element = WebDriverWait(driver, 10)\
        #     .until(ec.presence_of_element_located((By.ID, "header-details-user-fullname")))

        login_form_element = WebDriverWait(self.driver, 10)\
            .until(ec.presence_of_element_located((By.ID, "login-form-username")))

        # assert profile_logo_element.is_displayed(), "Profile logo element was not found"
        assert login_form_element.is_displayed()

        self.login_page.login_to_jira()

        assert self.main_page.logged_in()

    def teardown_method(self):
        self.driver.close()
