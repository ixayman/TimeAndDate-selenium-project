import unittest

from logic.unit_customization_page import UnitCustomizationPage
from logic.home_page import HomePage
from infra.utils import extract_temperature_unit
from test.base_test import BaseTest


class TestChangeWeatherUnits(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver.get(cls.config['Unit-Customization-Page'])
        cls.unit_customization_page = UnitCustomizationPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_change_temperature_units(self):
        self.unit_customization_page.select_temperature_units('°Fahrenheit')
        self.unit_customization_page.click_save_settings_button()
        self.driver.get(self.config['home_page'])
        self.home_page = HomePage(self.driver)
        self.assertIn(extract_temperature_unit(self.home_page.get_current_home_temperature()),
                      '°Fahrenheit')


if __name__ == '__main__':
    unittest.main()
