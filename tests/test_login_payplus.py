import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.login
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver, request):
        # Print the name of the currently running test
        test_name = request.node.name
        logger.info(f"Running test: {test_name}")

        # Example of setting up browser options (if needed)
        options = Options()
        options.add_argument("--start-maximized")  # Start browser maximized
        options.add_argument("--disable-popup-blocking")  # Disable popup blocking
        yield

        # Teardown steps (if needed)
        # e.g., closing browser, cleaning up data, etc.
        logger.info(f"Finished test: {test_name}")

    def test_user_login_no_keep_me_connected(self, driver, page):
        driver.get("https://myaccount.payplus.co.il/login")
        page.send_keys_to_element(By.ID, "login-email", "andrey04051995@gmail.com")
        page.send_keys_to_element(By.ID, "login-password", "123456TEST")
        page.click_element(By.XPATH, '//button[@type="submit"]')

    def test_user_login_keep_me_connected(self, driver, page):
        driver.get("https://myaccount.payplus.co.il/login")
        page.send_keys_to_element(By.ID, "login-email", "andrey04051995@gmail.com")
        page.send_keys_to_element(By.ID, "login-password", "123456TEST")

        page.click_element(By.CSS_SELECTOR, 'div[role="checkbox"]')
        page.click_element(By.XPATH, '//button[@type="submit"]')

    def test_user_login_forget_password(self, driver, page):
        driver.get("https://myaccount.payplus.co.il/login")
        page.click_element(By.CSS_SELECTOR, "button.payplus-button-link")