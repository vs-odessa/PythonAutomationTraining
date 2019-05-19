from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestJira:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    def test_login_to_jira(self):
        self.login_page.open()
        assert self.login_page.at_page()
        assert self.login_page.login_form_presented()
        self.login_page.login_to_jira()
        assert self.main_page.logged_in()

    def teardown_method(self):
        self.driver.close()
