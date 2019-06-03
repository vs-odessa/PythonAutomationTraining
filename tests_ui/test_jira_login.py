import sys
sys.path.append('.')
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage
from functions.test_helper import attach_screenshot
import allure
import pytest


@pytest.mark.ui
class TestLoginJira:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    @allure.tag('ui')
    @allure.title('Login to Jira - positive')
    def test_login_to_jira_positive(self):
        self.login_page.open()
        assert self.login_page.at_page()
        assert self.login_page.login_form_presented()
        self.login_page.login_to_jira(self.login_page.MY_NAME, self.login_page.MY_PASS)
        assert self.main_page.logged_in()

    @allure.tag('ui')
    @allure.title('Login to Jira - wrong username')
    def test_login_to_jira_wrong_username(self):
        self.login_page.open()
        assert self.login_page.at_page()
        assert self.login_page.login_form_presented()
        self.login_page.login_to_jira("wrongusername", self.login_page.MY_PASS)
        assert self.login_page.auth_failed()

    @allure.tag('ui')
    @allure.title('Login to Jira - wrong username + Screenshot')
    def test_login_to_jira_wrong_username(self):
        self.login_page.open()
        assert self.login_page.at_page()
        assert self.login_page.login_form_presented()
        self.login_page.login_to_jira("wrongusername", self.login_page.MY_PASS)
        attach_screenshot(self.driver)
        assert self.login_page.auth_failed()

    @allure.tag('ui')
    @allure.title('Login to Jira - wrong password + Screenshot')
    def test_login_to_jira_wrong_password(self):
        self.login_page.open()
        assert self.login_page.at_page()
        assert self.login_page.login_form_presented()
        self.login_page.login_to_jira(self.login_page.MY_NAME, "wrongpassword")
        attach_screenshot(self.driver)
        assert self.login_page.auth_failed()

    def teardown_method(self):
        self.driver.close()
