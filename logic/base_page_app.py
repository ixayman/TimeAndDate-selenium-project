import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from infra.base_page import BasePage


class BasePageApp(BasePage):
    MAIN_LOGO = '//div[@class="tad-logo"]'
    ACCOUNT_HOVER = '//span[text()="My Account"]'
    MENU_ITEM_LIST = '//li[contains(@class, "site-nav__menu")]'
    SEARCH_BUTTON = '//i[@class="i-font i-search"]'
    SEARCH_FIELD = '//input[@id="site-nav-search"]'

    # HIDDEN HOVER
    SIGN_IN_POP_BUTTON = '//a[@id="poplogin"]'
    SIGN_OUT_POP_BUTTON = '//a[@id="popout"]'
    MY_LOCATION_POP_BUTTON = '//a[@id="popchi"]'
    MY_EVENTS_POP_BUTTON = '//a[text()="My Events"]'

    # HIDDEN POPUP
    EMAIL_FIELD = '//input[@id="email"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    SIGN_IN_BUTTON = '//input[@id="create"]'
    INVALID_LOGIN_MESSAGE = '//div[@id="errormessage"]'
    CITY_NAME_FIELD = '//input[@id="ftztxt"]'
    CITY_SAVE_BUTTON = '//button[@id="tzq_save"]'
    CITY_AUTO_FILL_LIST = './/ul[@class="asu"]//li'
    CITY_AUTO_FILL_LIST_ITEM_NAME = '//span[@class="ash"]'
    CITY_AUTO_FILL_LIST_ITEM_COUNTRY = '//span[@class="mnx"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._main_logo = driver.find_element(By.XPATH, self.MAIN_LOGO)
        self._account_hover = self._driver.find_element(By.XPATH, self.ACCOUNT_HOVER)
        self._menu_item_list = self._driver.find_elements(By.XPATH, self.MENU_ITEM_LIST)
        self._news_menu = self._menu_item_list[0]
        self._world_clock_menu = self._menu_item_list[1]
        self._time_zone_menu = self._menu_item_list[2]
        self._calendar_menu = self._menu_item_list[3]
        self._weather_menu = self._menu_item_list[4]
        self._sun_and_moon_menu = self._menu_item_list[5]
        self._timers_menu = self._menu_item_list[6]
        self._calculator_menu = self._menu_item_list[7]
        self._search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def click_main_logo(self):
        self._main_logo.click()

    def hover_on_account_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._account_hover).perform()

    def click_account_menu(self):
        self._account_hover.click()

    def hover_on_news_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._news_menu).perform()

    def click_news_link(self):
        self._news_menu.click()

    def hover_on_world_clock_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._world_clock_menu).perform()

    def click_world_clock_link(self):
        self._world_clock_menu.click()

    def hover_on_time_zone_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._time_zone_menu).perform()

    def click_time_zone_link(self):
        self._time_zone_menu.click()

    def hover_on_calendar_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._calendar_menu).perform()

    def click_calendar_link(self):
        self._calendar_menu.click()

    def hover_on_weather_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._weather_menu).perform()

    def click_weather_link(self):
        self._weather_menu.click()

    def hover_on_sun_and_moon_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._sun_and_moon_menu).perform()

    def click_sun_and_moon_link(self):
        self._sun_and_moon_menu.click()

    def hover_on_timers_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._timers_menu).perform()

    def click_timers_link(self):
        self._timers_menu.click()

    def hover_on_calculator_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._calculator_menu).perform()

    def click_calculator_link(self):
        self._calculator_menu.click()

    # -----------------------------------------------------------------------------------------------------
    def click_my_location_pop_button(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.MY_LOCATION_POP_BUTTON)), message="My location pop up button not found").click()

    def insert_in_city_name_field(self, value):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.CITY_NAME_FIELD)), message="City name field not found")
        field = self._driver.find_element(By.XPATH, self.CITY_NAME_FIELD)
        field.clear()
        field.send_keys(value)

    def get_city_auto_fill_list(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.CITY_AUTO_FILL_LIST)), message="City auto fill list not found")
        return self._driver.find_elements(By.XPATH, self.CITY_AUTO_FILL_LIST)

    def get_city_auto_fill_list_item_name(self, item):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.CITY_AUTO_FILL_LIST_ITEM_NAME)), message="City auto fill list item name not found")
        return item.find_element(By.XPATH, self.CITY_AUTO_FILL_LIST_ITEM_NAME).text

    def get_city_auto_fill_list_item_country(self, item):
        WebDriverWait(item, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.CITY_AUTO_FILL_LIST_ITEM_NAME)), message="City auto fill list item country not found")
        return item.find_element(By.XPATH, self.CITY_AUTO_FILL_LIST_ITEM_COUNTRY).text

    @staticmethod
    def click_city_auto_fill_list_item(self, item):
        item.click()

    def click_city_save_button(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.CITY_SAVE_BUTTON)), message="City save button not found").click()

    # -----------------------------------------------------------------------------------------------------
    def click_sign_in_pop_button(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.SIGN_IN_POP_BUTTON)), message="Sign in pop up button not found").click()

    def insert_in_email_field(self, value):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.EMAIL_FIELD)), message="Email field not found")
        field = self._driver.find_element(By.XPATH, self.EMAIL_FIELD)
        field.clear()
        field.send_keys(value)

    def insert_in_password_field(self, value):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.PASSWORD_FIELD)), message="Password field not found")
        field = self._driver.find_element(By.XPATH, self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(value)

    def click_sign_in_button(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.SIGN_IN_BUTTON)), message="Sign in button not found")
        button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
        button.click()

    def is_invalid_login_message_displayed(self):
        try:
            invalid_login_message = self._driver.find_element(By.XPATH, self.INVALID_LOGIN_MESSAGE)
            invalid_login_message.is_displayed()
            return True
        except NoSuchElementException:
            return False

    def is_sign_out_Pop_displayed(self):
        try:
            sign_out_pop_button = self._driver.find_element(By.XPATH, self.SIGN_OUT_POP_BUTTON)
            sign_out_pop_button.is_displayed()
            return True
        except NoSuchElementException:
            return False

    # -----------------------------------------------------------------------------------------------------
    def click_search_button(self):
        self._search_button.click()

    def insert_in_search_field(self, value):
        field = self._driver.find_element(By.XPATH, self.SEARCH_FIELD)
        field.clear()
        field.send_keys(value)

    # -----------------------------------------------------------------------------------------------------

    def click_my_events_pop_button(self):
        WebDriverWait(self._driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, self.MY_EVENTS_POP_BUTTON)), message="My events pop up button not found").click()

    # -----------------------------------------------------------------------------------------------------

    def is_locked_login_message_displayed(self):
        """
        Check if login is locked by website
        :return:
        """
        try:
            locked_login_message = (
                self._driver.find_element(By.XPATH,'//div[text()="Too many account creations; please wait a while."]'))
            locked_login_message.is_displayed()
            return True
        except NoSuchElementException:
            return False

    def login_flow(self, email, password):
        """
        Login flow - login with account email and password
        :param email: account email
        :param password: account password
        :return: None
        """
        self.hover_on_account_menu()
        self.click_sign_in_pop_button()
        self.insert_in_email_field(email)
        self.insert_in_password_field(password)
        self.click_sign_in_button()
        time.sleep(2)
        if self.is_locked_login_message_displayed():
            print("login locked by website")
            self._driver.close()
            exit(-1)
