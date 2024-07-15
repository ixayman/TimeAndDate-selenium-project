import pickle
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from logic.utils import accept_cookies_pop


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the class-level fixtures for the test.
        - Initializes the logger.
        - Loads configuration settings.
        - Starts the browser and loads cookies.
        - Refreshes the page to apply the cookies.
        """
        cls.logger = Logger.setup_logger(__name__)
        cls.config = ConfigProvider.load_from_file()
        cls.logger.info("-" * 26)  # Separator line at the start of each test run
        cls.logger.info("Loading configuration")
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver(cls.config, "home_page")
        cls.logger.info("Browser opened - load cookies")
        # Accept cookies pop-up if present
        accept_cookies_pop(cls.driver)
        try:
            # Load cookies from file
            with open('../cookies.pkl', 'rb') as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    cls.driver.add_cookie(cookie)
            cls.logger.info("Cookies loaded")
        except Exception as e:
            cls.logger.error("Error loading cookies: %s", e)
            raise
        # Refresh the browser to apply cookies
        cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close_driver()
