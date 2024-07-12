import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.search_results_page import SearchResultsPage


class TestSearchResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.search_results_page = SearchResultsPage(cls.driver)
        cls.config = ConfigProvider.load_from_file()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_search_results(self):
        self.search_results_page.click_search_button()
        self.search_results_page.insert_in_search_field(self.config["city"])
        self.search_results_page.click_search_button()
        self.search_results_page = SearchResultsPage(self.driver)
        results = self.search_results_page.get_search_results_list()
        for result in results:
            self.assertIn(self.config["city"].lower(), self.search_results_page.get_result_title(result).lower())
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
