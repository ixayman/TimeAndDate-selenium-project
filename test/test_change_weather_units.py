import unittest

from infra.logger import Logger
from logic.unit_customization_page import UnitCustomizationPage
from logic.home_page import HomePage
from infra.utils import extract_temperature_unit
from test.base_test import BaseTest


class TestChangeWeatherUnits(BaseTest):
    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment for changing weather units.
        Navigate to the Unit Customization Page and initialize the page object.
        """
        super().setUpClass()
        cls.logger = Logger.setup_logger(__name__)
        cls.logger.info("Navigating to Unit Customization Page")
        cls.driver.get(cls.config['Unit-Customization-Page'])
        cls.unit_customization_page = UnitCustomizationPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_change_temperature_units(self):
        """
        Test changing the temperature units to Fahrenheit.
        """
        self.logger.info("Changing temperature units to °Fahrenheit")
        self.unit_customization_page.select_temperature_units('°Fahrenheit')
        self.unit_customization_page.click_save_settings_button()
        self.logger.info("Navigating to Home Page to verify changes")
        self.driver.get(self.config['home_page'])
        self.home_page = HomePage(self.driver)
        current_unit = extract_temperature_unit(self.home_page.get_current_home_temperature())
        self.logger.info(f"Current temperature unit: {current_unit}")
        self.assertIn(current_unit, '°Fahrenheit')
        self.logger.info("Temperature unit changed successfully")


if __name__ == '__main__':
    unittest.main()
