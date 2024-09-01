import pytest
from selenium.webdriver.common.by import By

from conftest import logger

@pytest.mark.register
class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.test_name = request.node.name
        logger.info(f"Starting test: {self.test_name}")
        yield
        logger.info(f"Ending test: {self.test_name}")

    def test_user_registration_button_exists(self, driver, page):
        logger.info("Navigating to developers page")
        driver.get("https://www.payplus.co.il/developers#dev")
        page.wait_for_element(By.XPATH, '//a[@href="/signup"]')

        elements = driver.find_elements(By.XPATH, '//a[@href="/signup"]')
        if elements:
            logger.info("Clicking the registration button")
            elements[1].click()
        else:
            logger.error("Registration button not found")

    def test_user_registration_fill_details(self, driver, page):
        logger.info("Navigating to the signup page")
        driver.get("https://www.payplus.co.il/signup")

        logger.info("Filling in user details")
        page.send_keys_to_element(By.ID, 'input-35', "Andrey")
        page.send_keys_to_element(By.ID, 'input-38', "Tupikov")

        page.click_element(By.ID, 'input-42')

        logger.info("Selecting birthday")
        page.click_element(By.XPATH, "//ul[@class='v-date-picker-years']/li[text()='1995']")
        page.click_element(By.XPATH, '//div[contains(@class, "v-btn__content") and text()="מאי"]')
        page.click_element(By.XPATH, '//div[@class="v-btn__content" and text()="4"]')
        page.click_element(By.XPATH, "//span[@class='v-btn__content' and contains(text(), 'OK')]")

        logger.info("Filling phone number section")
        page.send_keys_to_element(By.ID, 'input-46', "ישראל")
        page.click_element(By.XPATH, '//img[@src="/_nuxt/img/il.73efcec.svg"]')
        page.send_keys_to_element(By.ID, "input-51", "508117980")

        page.send_keys_to_element(By.ID, "input-54", "andrey04051995@gmail.com")

        logger.info("Submitting registration form")
        page.click_element(By.XPATH, '//button[@class="next-btn w-100" and normalize-space()="המשך"]')
        logger.info("Details filled successfully!")
