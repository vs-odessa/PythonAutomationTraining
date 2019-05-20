from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep


class EditIssuePage:

    ISSUE_SUMMARY_FIELD = (By.ID, "summary")
    ISSUE_DESCRIPTION_FIELD = (By.ID, "description")
    ASSIGN_TO_ME_TRIGGER_LINK = (By.ID, "assign-to-me-trigger")
    PRIORITY_FIELD = (By.ID, "priority-field")
    CREATE_ISSUE_SUBMIT_BUTTON = (By.ID, "create-issue-submit")
    UPDATE_ISSUE_SUBMIT_BUTTON = (By.ID, "edit-issue-submit")
    ISSUE_UPDATED_MESSAGE = (By.ID, "aui-flag-container")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

    def __init__(self, driver):
        self.driver = driver

    def set_issue_summary(self, summary_text):
        self.driver.find_element(*self.ISSUE_SUMMARY_FIELD).send_keys(summary_text)

    def set_issue_body(self, body_text):
        create_issue_textarea: WebElement = self.driver.find_element(*self.ISSUE_DESCRIPTION_FIELD)
        self.driver.switchTo().frame(self.driver.findElement(By.id("mce_0_ifr")))
        self.driver.find_element(*self.ISSUE_DESCRIPTION_FIELD).send_keys(body_text)
        create_issue_textarea.send_keys(Keys.ENTER)
        create_issue_textarea.clear()

        create_issue_textarea.send_keys(body_text)
        self.driver.switchTo().defaultContent()

    def assign_to_current_user(self):
        self.driver.find_element(*self.ASSIGN_TO_ME_TRIGGER_LINK).click()

    def set_priority_value(self, value):
        priority_element: WebElement = self.driver.find_element(*self.PRIORITY_FIELD)
        # select = Select(priority_element)
        # select.select_by_value(value)
        sleep(0.5)
        priority_element.send_keys(value)
        sleep(2)
        priority_element.send_keys(Keys.ENTER)
        sleep(2)

    def submit_create_issue(self):
        create_issue_submit_button: WebElement = self.driver.find_element(*self.CREATE_ISSUE_SUBMIT_BUTTON)
        create_issue_submit_button.click()

    def submit_update_issue(self):
        update_issue_submit_button: WebElement = self.driver.find_element(*self.UPDATE_ISSUE_SUBMIT_BUTTON)
        update_issue_submit_button.click()

    def issue_updated_message_appeared(self):
        # message_updated_element: WebElement = self.driver.find_element(*self.ISSUE_UPDATED_MESSAGE)
        element_found = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.ISSUE_UPDATED_MESSAGE))
        return element_found

    def error_occurred(self):
        error_message: WebElement = self.driver.find_element(*self.ERROR_MESSAGE)
        return error_message.is_displayed()
