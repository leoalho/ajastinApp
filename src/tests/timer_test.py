import unittest
from entities.timer import Timer

class TestTimer(unittest.TestCase):
    def setUp(self) -> None:
        self.timer = Timer()

    def test_tick_adds_current_time_by_one(self):
        self.timer.tick()
        self.assertEqual(self.timer.get_current_time(), "1 s")

    def test_reset_sets_time_to_zero(self):
        self.timer.tick()
        self.timer.reset()
        self.assertEqual(self.timer.get_current_time(), "0 s")
    
    def test_toggle_timer_changes_timer_on_value(self):
        self.timer.toggle_timer()
        self.assertEqual(self.timer.timer_on, True)

    def test_toggle_timer_twice_does_not_change_timer_on_value(self):
        self.timer.toggle_timer()
        self.timer.toggle_timer()
        self.assertEqual(self.timer.timer_on, False)

    def test_session_time_gets_updated_when_resetting(self):
        self.timer.tick()
        self.timer.reset()
        self.assertEqual(self.timer.get_session_time(), "1 s")