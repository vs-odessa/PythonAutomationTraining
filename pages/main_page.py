from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep


class MainPage:
    driver = None
    CREATE_ISSUE_BUTTON = (By.ID, "create_link")
    QUICK_SEARCH_INPUT = (By.ID, "quickSearchInput")
    QUICK_SEARCH_RESULT_ITEM = (By.CLASS_NAME, "quick-search-result-item")
    RESULT_ITEM = (By.CLASS_NAME, "quick-search-result-item")

    def __init__(self, driver):
        self.driver = driver

    def logged_in(self):
        profile_logo_element = WebDriverWait(self.driver, 10) \
            .until(ec.presence_of_element_located((By.ID, "header-details-user-fullname")))
        return profile_logo_element.is_displayed()

    def click_create_issue_button(self):
        # WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(*self.CREATE_ISSUE_BUTTON)).click()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.CREATE_ISSUE_BUTTON)).click()
        # self.driver.find_element(*self.CREATE_ISSUE_BUTTON).click()

    def perform_search(self, search_text):
        search_field: WebElement = self.driver.find_element(*self.QUICK_SEARCH_INPUT)
        search_field.send_keys(search_text)
        sleep(3)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.RESULT_ITEM)).click()

        # search_field.send_keys(Keys.ARROW_DOWN)
        # self.driver.implicitly_wait(5)
        # search_field.send_keys(Keys.ENTER)
        sleep(3)


