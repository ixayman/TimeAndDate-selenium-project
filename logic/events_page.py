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
    INDIVIDUAL_EVENT_LIST = './/div[@class="sidebar__event-list"]'
    INDIVIDUAL_EVENT_LIST_DELETE_BUTTON = '//a[@class="i-font i-delete fadeIn"]'
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

    def get_event_lists(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located((By.XPATH, self.EVENTS_LISTS)))
        events_lists = self._driver.find_element(By.XPATH, self.EVENTS_LISTS)
        return events_lists.find_elements(By.XPATH, self.INDIVIDUAL_EVENT_LIST)

    def hover_on_individual_event_list(self, event_list):
        # WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(event_list))
        ActionChains(self._driver).move_to_element(event_list).perform()

    def click_individual_event_list_delete_button(self, event_list):
        delete_button = (WebDriverWait(self._driver, 10).
                         until(ec.element_to_be_clickable((By.XPATH, self.INDIVIDUAL_EVENT_LIST_DELETE_BUTTON))))
        # self._driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)
        delete_button.click()

    def add_event_list_flow(self, name):
        self.click_add_event_list_button()
        self.insert_in_new_event_list_name_field(name)
        self.click_save_new_event_list_button()