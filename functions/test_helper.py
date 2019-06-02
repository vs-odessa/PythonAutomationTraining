import sys
sys.path.append('.')
import allure
from functions.data_helper import get_current_timestamp_string


def attach_screenshot(driver, name=""):
    if name == "":
        name = "screenshot" + get_current_timestamp_string()
    try:
        allure.attach(driver.get_screenshot_as_png(),
                      name=name,
                      attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(e)

