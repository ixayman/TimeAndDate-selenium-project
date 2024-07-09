from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec

from infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self._config = ConfigProvider.load_from_file()
        print("Test Start")

    def get_driver(self, page):
        try:
            browser = self._config.get("browser", "Firefox")  # Default to Firefox if not specified
            if browser == "Chrome":
                self._driver = webdriver.Chrome()
            elif browser == "Firefox":
                self._driver = webdriver.Firefox()
            elif browser == "Edge":
                self._driver = webdriver.Edge()
            else:
                raise ValueError(f"Unsupported browser: {browser}")

            url = self._config.get(page)
            if url:
                self._driver.maximize_window()
                self._driver.get(url)
                try:
                    WebDriverWait(self._driver, 10).until(
                        ec.presence_of_element_located((By.XPATH, '//body'))
                    )
                except TimeoutException:
                    print("Loading the page took too long!")
            else:
                print(f"Page '{page}' not found in the configuration.")
                exit(-1)
            return self._driver
        except WebDriverException as e:
            print(f"WebDriverException : {e}")
