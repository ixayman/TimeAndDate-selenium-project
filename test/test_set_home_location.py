import time
import unittest

from infra.logger import Logger
from logic.home_page import HomePage
from test.base_test import BaseTest


class TestSetHomeLocation(BaseTest):
    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment.
        - Initialize the logger.
        - Initialize the HomePage.
        """
        super().setUpClass()
        cls.logger = Logger.setup_logger(__name__)
        cls.logger.info("Initializing HomePage")
        cls.home_page = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_set_home_location_autofill(self):
        """
        Test setting the home location using the autofill feature.
        - Hover on the account menu and click the location pop-up button.
        - Insert city name and select from autofill list.
        - Save the new home location and verify the update.
        """
        try:
            self.logger.info("Starting test for setting home location with autofill")
            self.home_page.hover_on_account_menu()
            self.home_page.click_my_location_pop_button()
            self.home_page.insert_in_city_name_field(self.config["city-auto-fill"])
            for item in self.home_page.get_city_auto_fill_list():
                self.logger.info(f"Checking autofill item: {item.text.replace('\n', '-')}")
                if item.text == self.config["location"]:
                    self.logger.info(f"Matching item found, selecting it")
                    self.assertTrue(True, "Item found in list")
                    item.click()
                    break
            self.home_page.click_city_save_button()
            self.home_page = HomePage(self.driver)
            current_location = self.home_page.get_current_home_location()
            self.logger.info(f"Verifying if home location is updated to: {self.config['updated-location']}")
            self.assertEqual(self.config["updated-location"], current_location, "Home location not updated")
            self.logger.info("Home location test passed")
        except Exception as e:
            self.logger.error("An error occurred during the home location test: %s", e)
            raise


if __name__ == '__main__':
    unittest.main()
