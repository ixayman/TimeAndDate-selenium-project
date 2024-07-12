import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.base_page_app import BasePageApp


class TestMainCategoriesLinks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.config = ConfigProvider.load_from_file()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.base_page_app = BasePageApp(self.driver)

    def test_news_link(self):
        self.base_page_app.click_news_link()
        self.assertEqual(self.driver.current_url, self.config["news-page"])

    def test_world_clock_link(self):
        self.base_page_app.click_world_clock_link()
        self.assertEqual(self.driver.current_url, self.config["world-clock-page"])

    def test_time_zones_link(self):
        self.base_page_app.click_time_zone_link()
        self.assertEqual(self.driver.current_url, self.config["time-zone-page"])

    def test_calendar_link(self):
        self.base_page_app.click_calendar_link()
        self.assertEqual(self.driver.current_url, self.config["calendar-page"])

    def test_weather_link(self):
        self.base_page_app.click_weather_link()
        self.assertEqual(self.driver.current_url, self.config["weather-page"])

    def test_sun_and_moon_link(self):
        self.base_page_app.click_sun_and_moon_link()
        self.assertEqual(self.driver.current_url, self.config["sun-and-moon-page"])

    def test_timers_link(self):
        self.base_page_app.click_timers_link()
        self.assertEqual(self.driver.current_url, self.config["timers-page"])

    def test_calculator_link(self):
        self.base_page_app.click_calculator_link()
        self.assertEqual(self.driver.current_url, self.config["calculator-page"])


if __name__ == '__main__':
    unittest.main()
