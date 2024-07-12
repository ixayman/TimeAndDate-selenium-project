import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from logic.base_page_app import BasePageApp


class UnitCustomizationPage(BasePageApp):
    TEMPERATURE_UNITS_SELECTOR = '//select[@id="fut"]'
    PRESSURE_UNITS_SELECTOR = '//select[@id="fup"]'
    WINDSPEED_UNITS_SELECTOR = '//select[@id="fuw"]'
    DISTANCE_UNITS_SELECTOR = '//select[@id="fud"]'
    PRECIPITATION_UNITS_SELECTOR = '//select[@id="fur"]'
    SAVE_SETTINGS_BUTTON = '//input[@type="submit"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._temperature_units_selector = driver.find_element(By.XPATH, self.TEMPERATURE_UNITS_SELECTOR)
        self._pressure_units_selector = driver.find_element(By.XPATH, self.PRESSURE_UNITS_SELECTOR)
        self._windspeed_units_selector = driver.find_element(By.XPATH, self.WINDSPEED_UNITS_SELECTOR)
        self._distance_units_selector = driver.find_element(By.XPATH, self.DISTANCE_UNITS_SELECTOR)
        self._precipitation_units_selector = driver.find_element(By.XPATH, self.PRECIPITATION_UNITS_SELECTOR)

    def select_temperature_units(self, unit):
        select = Select(self._temperature_units_selector)
        select.select_by_visible_text(unit)

    def select_pressure_units(self, unit):
        select = Select(self._pressure_units_selector)
        select.select_by_visible_text(unit)

    def select_windspeed_units(self, unit):
        select = Select(self._windspeed_units_selector)
        select.select_by_visible_text(unit)

    def select_distance_units(self, unit):
        select = Select(self._distance_units_selector)
        select.select_by_visible_text(unit)

    def select_precipitation_units(self, unit):
        select = Select(self._precipitation_units_selector)
        select.select_by_visible_text(unit)

    def click_save_settings_button(self):
        self._driver.find_element(By.XPATH, self.SAVE_SETTINGS_BUTTON).click()
