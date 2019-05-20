from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class ViewIssuePage:

    ISSUE_SUMMARY_FIELD = (By.ID, "summary-val")
    # EDIT_ISSUE_BUTTON = (By.XPATH, "//*[@id=\"edit-issue\"]/span[2]")
    EDIT_ISSUE_BUTTON = (By.ID, "opsbar-edit-issue_container")

    def __init__(self, driver):
        self.driver = driver

    def get_issue_summary(self):
        issue_summary_element: WebElement = self.driver.find_element(*self.ISSUE_SUMMARY_FIELD)
        issue_summary_text = issue_summary_element.text
        return issue_summary_text

    def edit_current_issue(self):
        edit_issue_element = self.driver.find_element(*self.EDIT_ISSUE_BUTTON)
        edit_issue_element.click()