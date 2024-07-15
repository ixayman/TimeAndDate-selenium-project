import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from logic.base_page_app import BasePageApp


class EventsPage(BasePageApp):
    # Define XPATH locators for elements on the events page
    # init locators
    ADD_EVENT_LIST_BUTTON = '//button[@type="submit"]'
    MONTH_BLOCKS = '//div[@class="calendar__month-block"]'

    # visible locators
    MONTH_TITLE = './/h3[@class="calendar__month-title"]'
    DAY_NUMBER = './/a[@class="calendar__day-number"]'

    # hidden locators
    EVENTS_LISTS = '//div[@data-bind="foreach: Calendars"]'
    INDIVIDUAL_EVENT_LIST = './/div[@class="sidebar__event-list"]'
    INDIVIDUAL_EVENT_LIST_DELETE_BUTTON = './/a[@class="i-font i-delete fadeIn"]'
    CONFIRM_DELETE_EVENT_LIST_BUTTON = '//button[@type="submit"][text()="Delete"]'
    NEW_EVENT_LIST_BLOCK = '//div[@data-bind="if: CalendarAdding"]'
    NEW_EVENT_LIST_NAME_FIELD = '//input[@placeholder="Calendar Name"]'
    SAVE_NEW_EVENT_LIST_BUTTON = '//button[@data-bind="click: ConfirmCalendarAdd"]'

    ADD_EVENT_TITLE_FIELD = '//input[@class="addevent-modal__summary"]'
    EVENT_LIST_SELECT = '//select[@id="cal"]'
    REPEAT_SELECT = '//select[@id="rrule_freq"]'
    DAY_INPUT_FIELD = '//input[@class="input-date__input"][@placeholder="dd"]'
    MONTH_INPUT_FIELD = '//input[@class="input-date__input"][@placeholder="mm"]'
    YEAR_INPUT_FIELD = '//input[@class="input-date__input"][@placeholder="yyyy"]'
    ADD_EVENT_BUTTON = '//button[@type="submit"][text()="Add"]'

    ACTIVE_EVENT_TITLE = '//span[@data-bind="text:title"]'
    ACTIVE_EVENT_CANCEL_BUTTON = '//button[text()="Cancel"]'

    def __init__(self, driver):
        super().__init__(driver)
        # Initialize the elements
        self._add_event_list_button = driver.find_element(By.XPATH, self.ADD_EVENT_LIST_BUTTON)
        self._month_blocks = driver.find_elements(By.XPATH, self.MONTH_BLOCKS)

    # ----------------------------------------------------------------------------------------------------
    def click_add_event_list_button(self):
        self._driver.find_element(By.XPATH, self.ADD_EVENT_LIST_BUTTON).click()

    def insert_in_new_event_list_name_field(self, name):
        # Insert text into the new event list name field
        WebDriverWait(self._driver, 10).until(ec.
                                              element_to_be_clickable((By.XPATH, self.NEW_EVENT_LIST_NAME_FIELD)))
        self._driver.find_element(By.XPATH, self.NEW_EVENT_LIST_NAME_FIELD).clear()
        self._driver.find_element(By.XPATH, self.NEW_EVENT_LIST_NAME_FIELD).send_keys(name)

    def click_save_new_event_list_button(self):
        # Click the button to save the new event list
        WebDriverWait(self._driver, 10).until(ec.
                                              element_to_be_clickable((By.XPATH, self.SAVE_NEW_EVENT_LIST_BUTTON)))
        self._driver.find_element(By.XPATH, self.SAVE_NEW_EVENT_LIST_BUTTON).click()

    def get_event_lists(self):
        # Get list of all event lists
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located((By.XPATH, self.EVENTS_LISTS)))
        events_lists = self._driver.find_element(By.XPATH, self.EVENTS_LISTS)
        return events_lists.find_elements(By.XPATH, self.INDIVIDUAL_EVENT_LIST)

    def hover_on_individual_event_list(self, event_list):
        ActionChains(self._driver).move_to_element(event_list).perform()

    def click_individual_event_list_delete_button(self, event_list):
        # Click the delete button for an individual event list
        delete_button = (WebDriverWait(event_list, 10).
                         until(ec.element_to_be_clickable((By.XPATH, self.INDIVIDUAL_EVENT_LIST_DELETE_BUTTON))))
        delete_button.click()

    def click_confirm_event_list_delete_button(self):
        # Click the button to confirm deletion of an event list
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable(
            (By.XPATH, self.CONFIRM_DELETE_EVENT_LIST_BUTTON)))
        self._driver.find_element(By.XPATH, self.CONFIRM_DELETE_EVENT_LIST_BUTTON).click()

    def add_event_list_flow(self, name):
        # Flow to add a new event list
        self.click_add_event_list_button()
        self.insert_in_new_event_list_name_field(name)
        self.click_save_new_event_list_button()
        time.sleep(5)

    def remove_event_list_flow(self, event_list):
        # Flow to remove an event list
        self.hover_on_individual_event_list(event_list)
        self.click_individual_event_list_delete_button(event_list)
        self.click_confirm_event_list_delete_button()
        time.sleep(5)

    def remove_event_list_by_name(self, name, lists):
        # Remove an event list by its name
        for list_item in lists:
            if list_item.text == name:
                self.remove_event_list_flow(list_item)

    # ----------------------------------------------------------------------------------------------------

    def get_month_blocks(self):
        return self._month_blocks

    def get_month_block_title(self, month_block):
        return month_block.find_element(By.XPATH, self.MONTH_TITLE).text

    def get_month_block(self, month):
        # Get a specific month block by month name
        for block in self._month_blocks:
            if block.find_element(By.XPATH, self.MONTH_TITLE).text == month:
                return block

    def click_day_number(self, day, month):
        # Click on a specific day number within a month block
        block = self.get_month_block(month)
        days = block.find_elements(By.XPATH, self.DAY_NUMBER)
        for d in days:
            if int(d.text) == day:
                d.click()
                return True
        return False

    def insert_in_add_event_title_field(self, title):
        # Insert text into the add event title field
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.ADD_EVENT_TITLE_FIELD)))
        self._driver.find_element(By.XPATH, self.ADD_EVENT_TITLE_FIELD).clear()
        self._driver.find_element(By.XPATH, self.ADD_EVENT_TITLE_FIELD).send_keys(title)

    def select_event_list(self, list_name):
        # Select an event list from the dropdown
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.EVENT_LIST_SELECT)))
        select = Select(self._driver.find_element(By.XPATH, self.EVENT_LIST_SELECT))
        select.select_by_visible_text(list_name)

    def select_repeat(self, repeat):
        # Select a repeat option from the dropdown
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.REPEAT_SELECT)))
        select = Select(self._driver.find_element(By.XPATH, self.REPEAT_SELECT))
        select.select_by_visible_text(repeat)

    def click_add_event_button(self):
        # Click the button to add an event
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.ADD_EVENT_BUTTON)))
        self._driver.find_element(By.XPATH, self.ADD_EVENT_BUTTON).click()
        time.sleep(2)

    def get_active_event_title(self):
        # Get the title of the active event
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located((By.XPATH, self.ACTIVE_EVENT_TITLE)))
        return self._driver.find_element(By.XPATH, self.ACTIVE_EVENT_TITLE).text

    def click_active_event_cancel_button(self):
        # Click the cancel button for the active event
        WebDriverWait(self._driver, 10).until(
            ec.presence_of_element_located((By.XPATH, self.ACTIVE_EVENT_CANCEL_BUTTON)))
        self._driver.find_element(By.XPATH, self.ACTIVE_EVENT_CANCEL_BUTTON).click()

    def check_if_monthly_recurring_event_created(self, month_number, day_number, random_title, month_blocks):
        """
        Check if a monthly recurring event was created successfully
        :param month_number:
        :param day_number:
        :param random_title:
        :param month_blocks:
        :return: true if event is found in all months, false otherwise
        """
        for month_block in month_blocks[month_number - 1:]:
            if self.click_day_number(day_number, self.get_month_block_title(month_block)):
                event_title = self.get_active_event_title()
                if event_title != random_title:
                    return False
                self.click_active_event_cancel_button()
        return True
