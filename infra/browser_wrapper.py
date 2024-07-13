from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec

from infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        print("Test Start")

    def get_driver(self, config, page):
        try:
            browser = config.get("browser", "Firefox")  # Default to Firefox if not specified
            if browser == "Chrome":
                self._driver = webdriver.Chrome()
            elif browser == "Firefox":
                self._driver = webdriver.Firefox()
            elif browser == "Edge":
                self._driver = webdriver.Edge()
            else:
                raise ValueError(f"Unsupported browser: {browser}")

            url = config.get(page)
            if url:
                self._driver.maximize_window()
                self._driver.get(url)
            else:
                print(f"Page '{page}' not found in the configuration.")
                exit(-1)
            return self._driver
        except WebDriverException as e:
            print(f"WebDriverException : {e}")
