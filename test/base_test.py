import pickle
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider

from logic.utils import accept_cookies_pop


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Load cookies from file and refresh the page
        :return:
        """
        cls.config = ConfigProvider.load_from_file()
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver(cls.config, "home_page")
        accept_cookies_pop(cls.driver)
        # Load cookies from file
        with open('../cookies.pkl', 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                cls.driver.add_cookie(cookie)
        cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
