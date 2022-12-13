import unittest
from services.main_service import MainService

class TestMainService(unittest.TestCase):
    def setUp(self):
        self.main_service = MainService()

    def test_no_user_and_timer_off_at_initialization(self):
        self.assertEqual(self.main_service.get_timer(), False)
        self.assertEqual(self.main_service.get_username(), None)

    def test_current_time_and_session_time_zero_at_intialization(self):
        self.assertEqual(self.main_service.get_current_time(), 0)
        self.assertEqual(self.main_service.get_session_time(), '0 s')

    def test_logging_in_creates_an_user(self):
        self.main_service.login("Test", "secret")
        self.assertEqual(self.main_service.get_username(), "Test")

    def test_user_has_one_project_after_logging_in(self):
        self.main_service.login("Test", "secret")
        self.assertEqual(len(self.main_service.get_projects()), 1)

    def test_logging_out_after_loggin_in_removes_current_user(self):
        self.main_service.login("Test", "secret")
        self.main_service.logout()
        self.assertEqual(self.main_service.get_username(), None)
