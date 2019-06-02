import sys
sys.path.append('.')
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage
from functions.test_helper import attach_screenshot


class TestLoginJira:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    def test_login_to_jira_positive(self):
        self.login_page.open()
        assert self.login_page.at_page()
        assert self.login_page.login_form_presented()
        self.login_page.login_to_jira(self.login_page.MY_NAME, self.login_page.MY_PASS)
        assert self.main_page.logged_in()

    def test_login_to_jira_wrong_username(self):
        self.login_page.open()
        assert self.login_page.at_page()
        assert self.login_page.login_form_presented()
        self.login_page.login_to_jira("wrongusername", self.login_page.MY_PASS)
        attach_screenshot(self.driver)
        assert self.login_page.auth_failed()

    def test_login_to_jira_wrong_password(self):
        self.login_page.open()
        assert self.login_page.at_page()
        assert self.login_page.login_form_presented()
        self.login_page.login_to_jira(self.login_page.MY_NAME, "wrongpassword")
        assert self.login_page.auth_failed()

    def teardown_method(self):
        self.driver.close()
