import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.PageObjectModel import PageObject

# Configure logging
# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create file handler for logging
file_handler = logging.FileHandler('test_log.log')
file_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


@pytest.fixture(scope="session")
def driver():
    logger.info("Setting up WebDriver")
    # Set up WebDriver (you can customize options as needed)
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--start-maximized")  # Start browser maximized

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    yield driver  # This provides the WebDriver instance to your tests
    logger.info("WebDriver quit")
    driver.quit()


@pytest.fixture(scope="session")
def page(driver):
    logger.info("Initializing PageObject")
    # Initialize the PageObject with the driver

    logger.info("PageObject initialized")
    return PageObject(driver)
