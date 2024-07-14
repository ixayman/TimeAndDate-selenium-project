import time
import unittest

from infra.utils import generate_random_string
from logic.events_page import EventsPage
from logic.home_page import HomePage
from test.base_test import BaseTest


class TestAddRemoveEventList(BaseTest):
    created_list_name = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.home_page = HomePage(cls.driver)
        cls.home_page.hover_on_account_menu()
        cls.home_page.click_my_events_pop_button()
        cls.events_page = EventsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # cls.events_page = EventsPage(cls.driver)
        lists = cls.events_page.get_event_lists()
        for list_item in lists:
            if list_item.text == cls.created_list_name:
                cls.events_page.remove_event_list_flow(list_item)
        cls.driver.close()

    def test_add_event_list(self):
        new_list_name = generate_random_string(5)
        TestAddRemoveEventList.created_list_name = new_list_name
        self.events_page.add_event_list_flow(new_list_name)
        self.events_page = EventsPage(self.driver)
        time.sleep(4)
        lists = self.events_page.get_event_lists()
        for list_item in lists:
            if list_item.text == new_list_name:
                self.assertTrue(True)
                break
        else:
            self.assertTrue(False)

    def test_add_remove_event_list(self):
        new_list_name = generate_random_string(5)
        self.events_page.add_event_list_flow(new_list_name)
        self.events_page = EventsPage(self.driver)
        time.sleep(2)
        lists = self.events_page.get_event_lists()
        for list_item in lists:
            if list_item.text == new_list_name:
                self.events_page.remove_event_list_flow(list_item)
                break
        self.events_page = EventsPage(self.driver)
        time.sleep(2)
        updated_lists = self.events_page.get_event_lists()
        for updated_list in updated_lists:
            if updated_list.text == new_list_name:
                self.assertTrue(False)
                break
        else:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
