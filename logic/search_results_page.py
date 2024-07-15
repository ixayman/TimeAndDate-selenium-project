from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class SearchResultsPage(BasePageApp):
    # Define XPATH locators for elements on the search results page
    SEARCH_RESULTS = '//article[contains(@class, "searchresult")]'
    RESULT_TITLE = './/div[@class="searchcap"]'

    def __init__(self, driver):
        super().__init__(driver)
        # Initialize the search results elements
        self._search_results = driver.find_elements(By.XPATH, self.SEARCH_RESULTS)

    def get_search_results_list(self):
        return self._search_results

    def get_result_title(self, result):
        return result.find_element(By.XPATH, self.RESULT_TITLE).text

