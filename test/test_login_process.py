import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from infra.utils import generate_random_email, generate_random_string
from logic.base_page_app import BasePageApp


class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.
        - Load configuration settings.
        - Start the browser and initialize the BasePageApp.
        """
        self.logger = Logger.setup_logger(__name__)
        self.config = ConfigProvider.load_from_file()
        self.logger.info("-" * 26)  # Separator line at the start of each test run
        self.logger.info("Loading configuration")
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config, "home_page")
        self.base_page_app = BasePageApp(self.driver)
        self.logger.info("Browser opened")

    def tearDown(self):
        self.browser.close_driver()

    def test_login_successfully(self):
        """
        Test logging in with valid credentials.
        """
        self.logger.info("Testing successful login")
        self.base_page_app.hover_on_account_menu()
        self.base_page_app.click_sign_in_pop_button()
        self.base_page_app.insert_in_email_field(self.config["email"])
        self.base_page_app.insert_in_password_field(self.config["password"])
        self.base_page_app.click_sign_in_button()
        self.base_page_app = BasePageApp(self.driver)
        self.base_page_app.hover_on_account_menu()
        self.assertTrue(self.base_page_app.is_sign_out_Pop_displayed())
        self.logger.info("Login successful")

    def test_login_invalid_email(self):
        """
        Test logging in with an invalid email.
        """
        self.logger.info("Testing login with invalid email")
        self.base_page_app.hover_on_account_menu()
        self.base_page_app.click_sign_in_pop_button()
        self.base_page_app.insert_in_email_field(generate_random_email())
        self.base_page_app.insert_in_password_field("password")
        self.base_page_app.click_sign_in_button()
        self.assertTrue(self.base_page_app.is_invalid_login_message_displayed())
        self.logger.info("Invalid email login test passed")

    def test_login_invalid_password(self):
        """
        Test logging in with an invalid password.
        """
        self.logger.info("Testing login with invalid password")
        self.base_page_app.hover_on_account_menu()
        self.base_page_app.click_sign_in_pop_button()
        self.base_page_app.insert_in_email_field(self.config["email"])
        self.base_page_app.insert_in_password_field(generate_random_string(8))
        self.base_page_app.click_sign_in_button()
        self.assertTrue(self.base_page_app.is_invalid_login_message_displayed())
        self.logger.info("Invalid password login test passed")


if __name__ == '__main__':
    unittest.main()
