from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from logic.base_page_app import BasePageApp


class HomePage(BasePageApp):
    # Define XPATH locators for elements on the home page
    SECTION_LIST = '//div[contains(@class,"tad-layout-row ")]'
    SECTION = '//section'
    TEMPERATURE = '//span[@class ="cur-temp nw"]'

    def __init__(self, driver):
        super().__init__(driver)
        # Initialize the elements
        self._section_list = driver.find_elements(By.XPATH, self.SECTION_LIST)
        self._current_time_section = self._section_list[0].find_elements(By.XPATH, self.SECTION)[0]
        self._time_zones_section = self._section_list[0].find_elements(By.XPATH, self.SECTION)[1]
        self._calendar_section = self._section_list[0].find_elements(By.XPATH, self.SECTION)[2]
        self._temperature = self._current_time_section.find_element(By.XPATH, self.TEMPERATURE)

    def get_current_home_location(self):
        # Get the current home location from the page
        WebDriverWait(self._current_time_section, 10).until(
            ec.presence_of_element_located((By.XPATH, '//p/a'))
        )
        return self._current_time_section.find_element(By.XPATH, '//p/a').text

    def get_current_home_temperature(self):
        return self._temperature.text
