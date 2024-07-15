import time
import unittest

from infra.logger import Logger
from infra.utils import generate_random_string
from logic.events_page import EventsPage
from logic.home_page import HomePage
from test.base_test import BaseTest


class TestAddRemoveEventList(BaseTest):
    created_list_name = None

    @classmethod
    def setUpClass(cls):
        """
        Set up events page and initialize the EventsPage.
        """
        super().setUpClass()
        cls.logger = Logger.setup_logger(__name__)
        cls.logger.info("Initializing HomePage and EventsPage")
        cls.home_page = HomePage(cls.driver)
        cls.home_page.hover_on_account_menu()
        cls.home_page.click_my_events_pop_button()
        cls.events_page = EventsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test and remove the created event list if it exists.
        """
        cls.logger.info("Tearing down test and removing created event list if exists")
        lists = cls.events_page.get_event_lists()
        cls.events_page.remove_event_list_by_name(cls.created_list_name, lists)
        super().tearDownClass()

    def test_add_event_list(self):
        """
        Test case to add an event list.
        """
        try:
            self.logger.info(f"starting test_add_event_list")
            new_list_name = generate_random_string(5)
            TestAddRemoveEventList.created_list_name = new_list_name
            self.logger.info(f"Adding event list with name: {new_list_name}")
            self.events_page.add_event_list_flow(new_list_name)
            self.events_page = EventsPage(self.driver)
            time.sleep(4)
            lists = self.events_page.get_event_lists()
            for list_item in lists:
                if list_item.text == new_list_name:
                    self.logger.info(f"Event list '{new_list_name}' added successfully")
                    self.assertTrue(True)
                    break
            else:
                self.logger.error(f"Event list '{new_list_name}' was not added")
                self.assertTrue(False)
        except Exception as e:
            self.logger.error(f"An error occurred during test_add_event_list: {e}")
            raise

    def test_add_remove_event_list(self):
        """
        Test case to add and then remove an event list.
        """
        try:
            self.logger.info(f"starting test_add_remove_event_list")
            new_list_name = generate_random_string(5)
            self.logger.info(f"Adding and then removing event list with name: {new_list_name}")
            self.events_page.add_event_list_flow(new_list_name)
            self.events_page = EventsPage(self.driver)
            lists = self.events_page.get_event_lists()
            for list_item in lists:
                if list_item.text == new_list_name:
                    self.events_page.remove_event_list_flow(list_item)
                    break
            self.events_page = EventsPage(self.driver)
            updated_lists = self.events_page.get_event_lists()
            for updated_list in updated_lists:
                if updated_list.text == new_list_name:
                    self.logger.error(f"Event list '{new_list_name}' was not removed")
                    self.assertTrue(False)
                    break
            else:
                self.logger.info(f"Event list '{new_list_name}' removed successfully")
                self.assertTrue(True)
        except Exception as e:
            self.logger.error(f"An error occurred during test_add_remove_event_list: {e}")
            raise


if __name__ == '__main__':
    unittest.main()
