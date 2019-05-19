from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def logged_in(self):
        profile_logo_element = WebDriverWait(self.driver, 10) \
            .until(ec.presence_of_element_located((By.ID, "header-details-user-fullname")))
        return profile_logo_element.is_displayed()
