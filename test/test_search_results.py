import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from logic.search_results_page import SearchResultsPage


class TestSearchResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment.
        - Initialize the logger.
        - Load configuration settings.
        - Start the browser and initialize SearchResultsPage.
        """
        cls.logger = Logger.setup_logger(__name__)
        cls.config = ConfigProvider.load_from_file()
        cls.logger.info("-" * 26)  # Separator line at the start of each test run
        cls.logger.info("Loading configuration")
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver(cls.config, "home_page")
        cls.search_results_page = SearchResultsPage(cls.driver)
        cls.logger.info("Browser opened and SearchResultsPage initialized")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close_driver()

    def test_search_results(self):
        """
        Test the search results functionality.
        - Perform a search for a specified city.
        - Verify that the search results contain the city name.
        """
        try:
            self.logger.info("Starting search results test")
            self.search_results_page.click_search_button()
            self.search_results_page.insert_in_search_field(self.config["city"])
            self.search_results_page.click_search_button()
            self.search_results_page = SearchResultsPage(self.driver)
            results = self.search_results_page.get_search_results_list()
            for result in results:
                result_title = self.search_results_page.get_result_title(result).lower()
                self.logger.info(f"Checking if '{self.config['city'].lower()}' is in '{result_title}'")
                self.assertIn(self.config["city"].lower(), result_title)
            self.logger.info("Search results test passed")
        except Exception as e:
            self.logger.error("An error occurred during the search results test: %s", e)
            raise


if __name__ == '__main__':
    unittest.main()
