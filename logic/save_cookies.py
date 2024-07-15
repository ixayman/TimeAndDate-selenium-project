import pickle

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider

from logic.base_page_app import BasePageApp
from logic.utils import accept_cookies_pop


def save_cookies():
    """
    run standalone to save login cookies
    """
    config = ConfigProvider.load_from_file()
    browser = BrowserWrapper()
    driver = browser.get_driver(config, "home_page")
    base_page_app = BasePageApp(driver)
    accept_cookies_pop(driver)
    base_page_app.login_flow(config['email'], config['password'])
    # Save cookies to file
    cookies = driver.get_cookies()
    with open('../cookies.pkl', 'wb') as file:
        pickle.dump(cookies, file)
    driver.quit()


save_cookies()
