import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.events_page import EventsPage
from logic.home_page import HomePage
from infra.utils import extract_temperature_unit,generate_random_string
from test.base_test import BaseTest


class TestSearchResults(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.home_page = HomePage(cls.driver)
        cls.home_page.hover_on_account_menu()
        cls.home_page.click_my_events_pop_button()
        cls.events_page = EventsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_add_event_list(self):
        new_list_name = generate_random_string(5)
        self.events_page.click_add_event_list_button()
        self.events_page.insert_in_new_event_list_name_field(new_list_name)
        self.events_page.click_save_new_event_list_button()
        self.events_page = EventsPage(self.driver)
        time.sleep(4)
        lists = self.events_page.get_event_lists()
        for list_item in lists:
            if list_item.text == new_list_name:
                self.assertTrue(True)
                break
        else:
            self.assertTrue(False)

    def test_remove_event_list(self):
        new_list_name = generate_random_string(5)
        self.events_page.add_event_list_flow(new_list_name)
        self.events_page = EventsPage(self.driver)
        time.sleep(4)
        lists = self.events_page.get_event_lists()
        for list in lists:
            if list.text == new_list_name:
                print(list.text)
                self.events_page.hover_on_individual_event_list(list)
                self.events_page.click_individual_event_list_delete_button(list)
                break
        self.events_page = EventsPage(self.driver)
        time.sleep(4)
        updated_lists = self.events_page.get_event_lists()
        for updated_list in updated_lists:
            print(updated_list.text)
            if updated_list.text == new_list_name:
                self.assertTrue(False)
                break
        else:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
