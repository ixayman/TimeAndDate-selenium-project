import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage


class TestSetHomeLocation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.home_page = HomePage(cls.driver)
        cls.config = ConfigProvider.load_from_file()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_Set_home_location_autofill(self):
        self.home_page.hover_on_account_menu()
        self.home_page.click_my_location_pop_button()
        self.home_page.insert_in_city_name_field(self.config["city-auto-fill"])
        for item in self.home_page.get_city_auto_fill_list():
            if item.text == self.config["location"]:
                item.click()
                break
        self.home_page.click_city_save_button()
        self.home_page = HomePage(self.driver)
        self.assertEqual(self.config["updated-location"], self.home_page.get_current_home_location())

    # def test_set_home_location(self):
    #     self.home_page.hover_on_account_menu()
    #     self.home_page.click_my_location_pop_button()
    #     self.home_page.insert_in_city_name_field(self.config["city"])
    #     self.home_page.get_city_auto_fill_list()[0].click()
    #     self.home_page.click_city_save_button()
    #     time.sleep(15)


if __name__ == '__main__':
    unittest.main()
