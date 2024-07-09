import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from infra.base_page import BasePage


0class BasePageApp(BasePage):
    ACCOUNT_HOVER = '//span[text()="My Account"]'
    MENU_ITEM_LIST = '//li[@class="site-nav__menu "]'
    SIGN_IN_POP = '//a[@id="poplogin"]'
    EMAIL_FIELD = '//input[@id="email"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    SIGN_IN_BUTTON = '//input[@id="create"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._account_hover = self._driver.find_element(By.XPATH, self.ACCOUNT_HOVER)

    def hover_on_account_menu(self):
        actions = ActionChains(self._driver)
        actions.move_to_element(self._account_hover).perform()

    def click_login_menu(self):
        sign_in = self._account_hover.find_element(By.XPATH, self.SIGN_IN_POP)
        sign_in.click()

    def insert_in_email_field(self,value):
        field = self._driver.find_element(By.XPATH, self.EMAIL_FIELD)
        field.clear()
        field.send_keys(value)

    def insert_in_password_field(self,value):
        field = self._driver.find_element(By.XPATH, self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(value)

    def click_sign_in_button(self):
        button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
        button.click()