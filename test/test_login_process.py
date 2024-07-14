import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import generate_random_email, generate_random_string
from logic.base_page_app import BasePageApp


class TestLoginProcess(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.config = ConfigProvider.load_from_file()
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver(cls.config, "home_page")
        cls.base_page_app = BasePageApp(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.close()

    def test_login_successfully(self):
        self.base_page_app.hover_on_account_menu()
        self.base_page_app.click_sign_in_pop_button()
        self.base_page_app.insert_in_email_field(self.config["email"])
        self.base_page_app.insert_in_password_field(self.config["password"])
        self.base_page_app.click_sign_in_button()
        time.sleep(2)
        self.base_page_app = BasePageApp(self.driver)
        self.base_page_app.hover_on_account_menu()
        self.assertTrue(self.base_page_app.is_sign_out_Pop_displayed())

    def test_login_invalid_email(self):
        self.base_page_app.hover_on_account_menu()
        self.base_page_app.click_sign_in_pop_button()
        self.base_page_app.insert_in_email_field(generate_random_email())
        self.base_page_app.insert_in_password_field("password")
        self.base_page_app.click_sign_in_button()
        self.assertTrue(self.base_page_app.is_invalid_login_message_displayed())

    def test_login_invalid_password(self):
        self.base_page_app.hover_on_account_menu()
        self.base_page_app.click_sign_in_pop_button()
        self.base_page_app.insert_in_email_field(self.config["email"])
        self.base_page_app.insert_in_password_field(generate_random_string(8))
        self.base_page_app.click_sign_in_button()
        self.assertTrue(self.base_page_app.is_invalid_login_message_displayed())


if __name__ == '__main__':
    unittest.main()
