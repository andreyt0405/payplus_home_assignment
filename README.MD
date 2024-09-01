# Selenium Testing with Pytest and API Testing using Requests

This repository contains a set of Selenium-based tests written in Python, using the Pytest framework. The tests are designed to automate the testing of various web pages, including user login, registration, and API calls related to payment processing.

## Prerequisites

- Python 3.8 or higher
- Google Chrome Browser
- ChromeDriver (ensure it matches your Chrome browser version)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/andreyt0405/payplus_home_assignment.git
   cd payplus_home_assignment

2. **Install requirements:**
   Before running the tests, you need to install the necessary dependencies. These are listed in the `requirements.txt` file. To install them, follow these steps:

   - **Install the required dependencies:**

     Once the virtual environment is activated, install the dependencies using the `requirements.txt` file:

     ```bash
     pip install -r requirements.txt
     ```
   
   This will install all the necessary packages required for running the tests.

3. **How to run it:**

   Running the tests is simple once you have the project open in PyCharm. Follow these steps:

   - **Open the project in PyCharm:**

     1. Launch PyCharm.
     2. Click on `File` > `Open...`.
     3. Navigate to the directory where you cloned the repository (`payplus_home_assignment`) and select it.
     4. Click `OK` to open the project.

   - **Configure Pytest in PyCharm:**

     1. Go to the top-right corner of PyCharm, where the run/debug configurations are listed, and click on `Edit Configurations...`.
     2. Click on the `+` icon to add a new configuration, then select `Python tests` > `pytest`.
     3. Set the `Target` to the project root or specific test files you want to run.
     4. Click `OK` to save the configuration.

   - **Run the tests:**

     Once the configuration is set, you can simply click the green run button next to the configuration dropdown to run all the tests using Pytest. The test results will be displayed in the PyCharm console.
