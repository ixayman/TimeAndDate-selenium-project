import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class BasePageApp(BasePage):
    MAIN_LOGO = '//div[@class="tad-logo"]'
    ACCOUNT_HOVER = '//span[text()="My Account"]'
    MENU_ITEM_LIST = '//li[@class="site-nav__menu "]'
    SEARCH_BUTTON = '//i [@class="i-font i-menu"]'
    SEARCH_FIELD = '//input[@id="site-nav-search"]'
    SIGN_IN_POP_UP_BUTTON = '//a[@id="poplogin"]'
    EMAIL_FIELD = '//input[@id="email"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    SIGN_IN_BUTTON = '//input[@id="create"]'

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

    def hover_on_news_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._news_menu).perform()

    def hover_on_world_clock_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._world_clock_menu).perform()

    def hover_on_time_zone_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._time_zone_menu).perform()

    def hover_on_calendar_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._calendar_menu).perform()

    def hover_on_weather_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._weather_menu).perform()

    def hover_on_sun_and_moon_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._sun_and_moon_menu).perform()

    def hover_on_timers_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._timers_menu).perform()

    def hover_on_calculator_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._calculator_menu).perform()

    def click_login_menu(self):
        sign_in = self._account_hover.find_element(By.XPATH, self.SIGN_IN_POP_UP_BUTTON)
        sign_in.click()

    def insert_in_email_field(self, value):
        field = self._driver.find_element(By.XPATH, self.EMAIL_FIELD)
        field.clear()
        field.send_keys(value)

    def insert_in_password_field(self, value):
        field = self._driver.find_element(By.XPATH, self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(value)

    def click_sign_in_button(self):
        button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
        button.click()

    def click_search_button(self):
        self._search_button.click()

    def insert_in_search_field(self, value):
        field = self._driver.find_element(By.XPATH, self.SEARCH_FIELD)
        field.clear()
        field.send_keys(value)