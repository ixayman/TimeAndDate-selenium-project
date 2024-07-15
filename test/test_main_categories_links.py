import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from logic.base_page_app import BasePageApp


class TestMainCategoriesLinks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment.
        - Initialize the logger.
        - Load configuration settings.
        - Start the browser and initialize BasePageApp.
        """
        cls.logger = Logger.setup_logger(__name__)
        cls.config = ConfigProvider.load_from_file()
        cls.logger.info("-" * 26)  # Separator line at the start of each test run
        cls.logger.info("Loading configuration")
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver(cls.config, "home_page")
        cls.logger.info("Browser opened and BasePageApp initialized")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close_driver()

    def setUp(self):
        """
        Set up the BasePageApp for each test.
        """
        self.base_page_app = BasePageApp(self.driver)

    def test_news_link(self):
        try:
            self.logger.info("Testing News link")
            self.base_page_app.click_news_link()
            self.assertEqual(self.driver.current_url, self.config["news-page"])
            self.logger.info("News link test passed")
        except Exception as e:
            self.logger.error(f"An error occurred during test_news_link: {e}")
            raise

    def test_world_clock_link(self):
        try:
            self.logger.info("Testing World Clock link")
            self.base_page_app.click_world_clock_link()
            self.assertEqual(self.driver.current_url, self.config["world-clock-page"])
            self.logger.info("World Clock link test passed")
        except Exception as e:
            self.logger.error(f"An error occurred during test_world_clock_link: {e}")
            raise

    def test_time_zones_link(self):
        try:
            self.logger.info("Testing Time Zones link")
            self.base_page_app.click_time_zone_link()
            self.assertEqual(self.driver.current_url, self.config["time-zone-page"])
            self.logger.info("Time Zones link test passed")
        except Exception as e:
            self.logger.error(f"An error occurred during test_time_zones_link: {e}")
            raise

    def test_calendar_link(self):
        try:
            self.logger.info("Testing Calendar link")
            self.base_page_app.click_calendar_link()
            self.assertEqual(self.driver.current_url, self.config["calendar-page"])
            self.logger.info("Calendar link test passed")
        except Exception as e:
            self.logger.error(f"An error occurred during test_calendar_link: {e}")
            raise

    def test_weather_link(self):
        try:
            self.logger.info("Testing Weather link")
            self.base_page_app.click_weather_link()
            self.assertEqual(self.driver.current_url, self.config["weather-page"])
            self.logger.info("Weather link test passed")
        except Exception as e:
            self.logger.error(f"An error occurred during test_weather_link: {e}")
            raise

    def test_sun_and_moon_link(self):
        try:
            self.logger.info("Testing Sun and Moon link")
            self.base_page_app.click_sun_and_moon_link()
            self.assertEqual(self.driver.current_url, self.config["sun-and-moon-page"])
            self.logger.info("Sun and Moon link test passed")
        except Exception as e:
            self.logger.error(f"An error occurred during test_sun_and_moon_link: {e}")
            raise

    def test_timers_link(self):
        try:
            self.logger.info("Testing Timers link")
            self.base_page_app.click_timers_link()
            self.assertEqual(self.driver.current_url, self.config["timers-page"])
            self.logger.info("Timers link test passed")
        except Exception as e:
            self.logger.error(f"An error occurred during test_timers_link: {e}")
            raise

    def test_calculator_link(self):
        try:
            self.logger.info("Testing Calculator link")
            self.base_page_app.click_calculator_link()
            self.assertEqual(self.driver.current_url, self.config["calculator-page"])
            self.logger.info("Calculator link test passed")
        except Exception as e:
            self.logger.error(f"An error occurred during test_calculator_link: {e}")
            raise


if __name__ == '__main__':
    unittest.main()
