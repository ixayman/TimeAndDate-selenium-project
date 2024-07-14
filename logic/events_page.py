from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from logic.base_page_app import BasePageApp


class EventsPage(BasePageApp):
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
        self._add_event_list_button = driver.find_element(By.XPATH, self.ADD_EVENT_LIST_BUTTON)
        self._month_blocks = driver.find_elements(By.XPATH, self.MONTH_BLOCKS)

    # ----------------------------------------------------------------------------------------------------
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
        delete_button = (WebDriverWait(event_list, 10).
                         until(ec.element_to_be_clickable((By.XPATH, self.INDIVIDUAL_EVENT_LIST_DELETE_BUTTON))))
        delete_button.click()

    def click_confirm_event_list_delete_button(self):
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable(
            (By.XPATH, self.CONFIRM_DELETE_EVENT_LIST_BUTTON)))
        self._driver.find_element(By.XPATH, self.CONFIRM_DELETE_EVENT_LIST_BUTTON).click()

    def add_event_list_flow(self, name):
        self.click_add_event_list_button()
        self.insert_in_new_event_list_name_field(name)
        self.click_save_new_event_list_button()

    def remove_event_list_flow(self, event_list):
        self.hover_on_individual_event_list(event_list)
        self.click_individual_event_list_delete_button(event_list)
        self.click_confirm_event_list_delete_button()

    # ----------------------------------------------------------------------------------------------------

    def get_month_blocks(self):
        return self._month_blocks

    def get_month_block_title(self, month_block):
        return month_block.find_element(By.XPATH, self.MONTH_TITLE).text

    def get_month_block(self, month):
        for block in self._month_blocks:
            if block.find_element(By.XPATH, self.MONTH_TITLE).text == month:
                return block

    def click_day_number(self, day, month):
        block = self.get_month_block(month)
        days = block.find_elements(By.XPATH, self.DAY_NUMBER)
        for d in days:
            if int(d.text) == day:
                d.click()
                return True
        return False

    def insert_in_add_event_title_field(self, title):
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.ADD_EVENT_TITLE_FIELD)))
        self._driver.find_element(By.XPATH, self.ADD_EVENT_TITLE_FIELD).clear()
        self._driver.find_element(By.XPATH, self.ADD_EVENT_TITLE_FIELD).send_keys(title)

    def select_event_list(self, list_name):
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.EVENT_LIST_SELECT)))
        select = Select(self._driver.find_element(By.XPATH, self.EVENT_LIST_SELECT))
        select.select_by_visible_text(list_name)

    def select_repeat(self, repeat):
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.REPEAT_SELECT)))
        select = Select(self._driver.find_element(By.XPATH, self.REPEAT_SELECT))
        select.select_by_visible_text(repeat)

    def insert_in_date_input_field(self, day, month, year):
        self._driver.find_element(By.XPATH, self.DAY_INPUT_FIELD).clear()

        self._driver.find_element(By.XPATH, self.DAY_INPUT_FIELD).send_keys(day)
        self._driver.find_element(By.XPATH, self.MONTH_INPUT_FIELD).clear()
        self._driver.find_element(By.XPATH, self.MONTH_INPUT_FIELD).send_keys(month)
        self._driver.find_element(By.XPATH, self.YEAR_INPUT_FIELD).clear()
        self._driver.find_element(By.XPATH, self.YEAR_INPUT_FIELD).send_keys(year)

    def click_add_event_button(self):
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.ADD_EVENT_BUTTON)))
        self._driver.find_element(By.XPATH, self.ADD_EVENT_BUTTON).click()

    def get_active_event_title(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located((By.XPATH, self.ACTIVE_EVENT_TITLE)))
        return self._driver.find_element(By.XPATH, self.ACTIVE_EVENT_TITLE).text

    def click_active_event_cancel_button(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located((By.XPATH, self.ACTIVE_EVENT_CANCEL_BUTTON)))
        self._driver.find_element(By.XPATH, self.ACTIVE_EVENT_CANCEL_BUTTON).click()
