import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.events_page import EventsPage
from logic.home_page import HomePage
from infra.utils import extract_temperature_unit


class TestSearchResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.home_page = HomePage(cls.driver)
        cls.config = ConfigProvider.load_from_file()
        cls.home_page.login_flow(cls.config['email'], cls.config['password'])
        cls.home_page = HomePage(cls.driver)
        cls.home_page.hover_on_account_menu()
        cls.home_page.click_my_events_pop_button()
        cls.events_page = EventsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_add_event_list(self):
        self.events_page.click_add_event_list_button()
        self.events_page.insert_in_new_event_list_name_field('test')
        self.events_page.click_save_new_event_list_button()



if __name__ == '__main__':
    unittest.main()
