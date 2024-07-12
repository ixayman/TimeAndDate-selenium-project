import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.unit_customization_page import UnitCustomizationPage
from logic.home_page import HomePage
from infra.utils import extract_temperature_unit


class TestSearchResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("Unit-Customization-Page")
        cls.unit_customization_page = UnitCustomizationPage(cls.driver)
        cls.config = ConfigProvider.load_from_file()
        cls.unit_customization_page.login_flow(cls.config['email'], cls.config['password'])
        cls.unit_customization_page = UnitCustomizationPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_change_temperature_units(self):
        self.unit_customization_page.select_temperature_units('°Fahrenheit')
        self.unit_customization_page.click_save_settings_button()
        self.unit_customization_page = UnitCustomizationPage(self.driver)
        self.unit_customization_page.click_main_logo()
        self.home_page = HomePage(self.driver)
        self.assertIn(extract_temperature_unit(self.home_page.get_current_home_temperature()),
                      '°Fahrenheit')


if __name__ == '__main__':
    unittest.main()
