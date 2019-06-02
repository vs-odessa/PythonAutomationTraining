from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.issue_edit_page import EditIssuePage
from pages.issue_view_page import ViewIssuePage
import allure
import pytest


@pytest.mark.ui
class TestIssueJira:

    # ISSUE_NAME = "Auto Issue Vladimir " + str(time())

    ISSUE_NAME = "Test Issue Vladimir"

    @allure.tag('ui')
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.edit_issue_page = EditIssuePage(self.driver)
        self.view_issue_page = ViewIssuePage(self.driver)

    @allure.tag('ui')
    def login_flow(self):
        self.login_page.open()
        self.login_page.login_to_jira()
        self.driver.implicitly_wait(5)
        assert self.main_page.logged_in()

    @allure.tag('ui')
    def test_create_issue_positive(self):
        self.login_page.open()
        self.login_page.login_to_jira()
        self.driver.implicitly_wait(5)
        assert self.main_page.logged_in()
        self.main_page.click_create_issue_button()
        self.edit_issue_page.set_issue_summary(self.ISSUE_NAME)
        # self.issue_page.set_issue_body("1 - Step1\n2 - Step2")
        self.edit_issue_page.assign_to_current_user()
        self.edit_issue_page.submit_create_issue()

    @allure.tag('ui')
    def test_create_issue_missing_required_field(self):
        self.login_flow()
        self.main_page.click_create_issue_button()
        # self.issue_page.set_issue_summary(self.ISSUE_NAME)
        self.edit_issue_page.submit_create_issue()
        assert self.edit_issue_page.error_occurred()

    @allure.tag('ui')
    def test_search_issue(self):
        self.login_flow()
        self.main_page.perform_search(self.ISSUE_NAME)
        summary: str = self.view_issue_page.get_issue_summary()
        assert summary.islower() == self.ISSUE_NAME.islower()

    @allure.tag('ui')
    def test_update_issue(self):
        self.login_flow()
        self.main_page.perform_search(self.ISSUE_NAME)
        self.view_issue_page.edit_current_issue()
        self.edit_issue_page.set_priority_value("High")
        self.edit_issue_page.submit_update_issue()
        assert self.edit_issue_page.issue_updated_message_appeared()

    @allure.tag('ui')
    def teardown_method(self):
        self.driver.close()
