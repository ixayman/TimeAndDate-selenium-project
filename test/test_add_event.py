import time
import unittest

from infra.utils import generate_random_string, get_month_name
from logic.events_page import EventsPage
from logic.home_page import HomePage
from test.base_test import BaseTest


class TestAddEvent(BaseTest):
    created_list_name = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.home_page = HomePage(cls.driver)
        cls.home_page.hover_on_account_menu()
        cls.home_page.click_my_events_pop_button()
        cls.events_page = EventsPage(cls.driver)
        cls.created_list_name = generate_random_string(7)
        cls.events_page.add_event_list_flow(cls.created_list_name)
        time.sleep(5)
        cls.events_page = EventsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.events_page = EventsPage(cls.driver)
        lists = cls.events_page.get_event_lists()
        for list_item in lists:
            if list_item.text == cls.created_list_name:
                cls.events_page.remove_event_list_flow(list_item)
        cls.driver.close()

    def test_add_event(self):

        # ----------------------------- arrange ------------------------------
        day_number = 21
        month_number = 2
        random_title = generate_random_string(5)

        # ---------------------------- act -----------------------------------
        self.events_page.click_day_number(day_number, get_month_name(month_number))
        self.events_page.insert_in_add_event_title_field(random_title)
        self.events_page.select_event_list(self.created_list_name)
        self.events_page.select_repeat("Monthly")
        self.events_page.click_add_event_button()
        time.sleep(2)
        self.events_page = EventsPage(self.driver)
        month_blocks = self.events_page.get_month_blocks()

        # --------------------------- assert ----------------------------------
        event_found = True
        for month_block in month_blocks[month_number - 1:]:
            if self.events_page.click_day_number(day_number, self.events_page.get_month_block_title(month_block)):
                event_title = self.events_page.get_active_event_title()
                if event_title != random_title:
                    event_found = False
                    break
                self.events_page.click_active_event_cancel_button()
        self.assertTrue(event_found, "Event not found")


if __name__ == '__main__':
    unittest.main()
