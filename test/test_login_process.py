import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.base_page_app import BasePageApp


class TestDeviceTheme(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.base_page_app = BasePageApp(cls.driver)
        cls.config = ConfigProvider()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_login_successfully(self):
        self.base_page_app.hover_on_account_menu()
        time.sleep(2)
        self.base_page_app.click_login_menu()
        time.sleep(2)
        self.base_page_app.insert_in_email_field("evoix.a@gmail.com")
        self.base_page_app.insert_in_password_field("Z789456123z")
        self.base_page_app.click_sign_in_button()
        time.sleep(10)





























if __name__ == '__main__':
    unittest.main()
