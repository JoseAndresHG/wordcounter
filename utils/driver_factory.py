import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    """Creates configured WebDriver instances for the test suite."""

    DEFAULT_TIMEOUT = 10

    @staticmethod
    def create_driver():
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")

        if os.getenv("HEADLESS", "false").lower() == "true":
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(0)

        return driver
