import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=20):
        """ Wait for an element to be present in the DOM. """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click_element(self, by, value):
        """ Click on an element after waiting for it to be present. """
        element = self.wait_for_element(by, value)
        time.sleep(1)
        element.click()

    def send_keys_to_element(self, by, value, keys):
        """ Clear the element and send keys to it. """
        time.sleep(1)
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(keys)

    def scroll_to_element(self, by, value, timeout=20):
        """ Scroll to an element and return it. """
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return element

    def wait_for_element_to_be_clickable(self, by, value, timeout=10):
        """ Wait for an element to be clickable. """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
