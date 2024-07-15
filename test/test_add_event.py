import unittest

from infra.logger import Logger
from infra.utils import generate_random_string, get_month_name
from logic.events_page import EventsPage
from logic.home_page import HomePage
from test.base_test import BaseTest


class TestAddEvent(BaseTest):
    created_list_name = None

    @classmethod
    def setUpClass(cls):
        """
        set up events page and create a new event list
        """
        super().setUpClass()
        cls.logger = Logger.setup_logger(__name__)
        try:
            # Navigate to events page
            cls.logger.info("Navigate to events page")
            cls.home_page = HomePage(cls.driver)
            cls.home_page.hover_on_account_menu()
            cls.home_page.click_my_events_pop_button()
            cls.events_page = EventsPage(cls.driver)

            # Create new event list
            cls.logger.info("Create new event list")
            cls.created_list_name = generate_random_string(7)
            cls.events_page.add_event_list_flow(cls.created_list_name)
            cls.events_page = EventsPage(cls.driver)
        except Exception as e:
            cls.logger.error("An error occurred during setUpClass: %s", e)
            raise

    @classmethod
    def tearDownClass(cls):
        """
        remove the created event list
        """
        try:
            cls.logger.info("Remove created event list")
            cls.events_page = EventsPage(cls.driver)
            lists = cls.events_page.get_event_lists()
            cls.events_page.remove_event_list_by_name(cls.created_list_name, lists)
        except Exception as e:
            cls.logger.error("An error occurred during tearDownClass: %s", e)
        finally:
            super().tearDownClass()  # Call the tearDownClass of BaseTest

    def test_add_monthly_event(self):
        """
        arrange: get chosen day number and month number
        act: click on the day number and add event with random title and choose monthly recurrence
        assert: go throw the months and check if the event is created
        """
        try:
            # Arrange
            self.logger.info("Arrange: get chosen day number and month number")
            day_number = self.config["day-of-event"]
            month_number = self.config["month-of-event"]
            random_title = generate_random_string(5)
            recurrence = self.config["monthly-recurrence-indicator"]

            # Act
            self.logger.info(
                "Act: click on the day number and add event with random title and choose monthly recurrence")
            self.events_page.click_day_number(day_number, get_month_name(month_number))
            self.events_page.insert_in_add_event_title_field(random_title)
            self.events_page.select_event_list(self.created_list_name)
            self.events_page.select_repeat(recurrence)
            self.events_page.click_add_event_button()
            self.events_page = EventsPage(self.driver)
            month_blocks = self.events_page.get_month_blocks()

            # Assert
            self.logger.info("Assert: go through the months and check if the event is created")
            self.assertTrue(self.events_page.check_if_monthly_recurring_event_created
                            (month_number, day_number, random_title, month_blocks), "Event not found")
        except Exception as e:
            self.logger.error("An error occurred during test_add_monthly_event: %s", e)
            raise


if __name__ == '__main__':
    unittest.main()
