import time
import unittest

from logic.home_page import HomePage
from test.base_test import BaseTest


class TestSetHomeLocation(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.home_page = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_set_home_location_autofill(self):
        self.home_page.hover_on_account_menu()
        self.home_page.click_my_location_pop_button()
        self.home_page.insert_in_city_name_field(self.config["city-auto-fill"])
        for item in self.home_page.get_city_auto_fill_list():
            if item.text == self.config["location"]:
                self.assertTrue(True, "Item found in list")
                item.click()
                break
        self.home_page.click_city_save_button()
        time.sleep(2)
        self.home_page = HomePage(self.driver)
        self.assertEqual(self.config["updated-location"], self.home_page.get_current_home_location(),
                         "Home location not updated")


if __name__ == '__main__':
    unittest.main()
