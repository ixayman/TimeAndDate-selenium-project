import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from logic.base_page_app import BasePageApp


class EventsPage(BasePageApp):
    # init locators
    ADD_EVENT_LIST_BUTTON = '//button[@type="submit"]'
    MONTH_BLOCKS = '//div[@class="calendar__month-block"]'

    # visible locators
    MONTH_TITLE = '//h3[@class="calendar__month-title"]'

    # hidden locators
    EVENTS_LISTS = '//div[@data-bind="foreach: Calendars"]'
    INDIVIDUAL_EVENT_LIST = '//div[@class="sidebar__event-list"]'
    NEW_EVENT_LIST_BLOCK = '//div[@data-bind="if: CalendarAdding"]'
    NEW_EVENT_LIST_NAME_FIELD = '//input[@placeholder="Calendar Name"]'
    SAVE_NEW_EVENT_LIST_BUTTON = '//button[@data-bind="click: ConfirmCalendarAdd"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_event_list_button = driver.find_element(By.XPATH, self.ADD_EVENT_LIST_BUTTON)
        self._month_blocks = driver.find_elements(By.XPATH, self.MONTH_BLOCKS)

    def click_add_event_list_button(self):
        self._driver.find_element(By.XPATH, self.ADD_EVENT_LIST_BUTTON).click()

    def insert_in_new_event_list_name_field(self, name):
        WebDriverWait(self._driver, 10).until(ec.
                                              element_to_be_clickable((By.XPATH, self.NEW_EVENT_LIST_NAME_FIELD)))
        self._driver.find_element(By.XPATH, self.NEW_EVENT_LIST_NAME_FIELD).clear()
        self._driver.find_element(By.XPATH, self.NEW_EVENT_LIST_NAME_FIELD).send_keys(name)

    def click_save_new_event_list_button(self):
        WebDriverWait(self._driver, 10).until(ec.
                                              element_to_be_clickable((By.XPATH, self.SAVE_NEW_EVENT_LIST_BUTTON)))
        self._driver.find_element(By.XPATH, self.SAVE_NEW_EVENT_LIST_BUTTON).click()
