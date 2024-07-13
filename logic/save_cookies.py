import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By

from infra.browser_wrapper import BrowserWrapper
from logic.base_page_app import BasePageApp
from infra.config_provider import ConfigProvider
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def save_cookies():
    config = ConfigProvider.load_from_file()
    browser = BrowserWrapper()
    driver = browser.get_driver(config, "home_page")
    base_page_app = BasePageApp(driver)
    try:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//span[text()="AGREE"]'))).click()
    except:
        pass
    base_page_app.login_flow(config['email'], config['password'])
    # Save cookies to file
    cookies = driver.get_cookies()
    with open('../cookies.pkl', 'wb') as file:
        pickle.dump(cookies, file)

    driver.quit()


save_cookies()
