import helpers
import unittest

class HelperTest(unittest.TestCase):
    def test_time_to_string_when_time_is_zero(self):
        zero = helpers.time_to_string(0)
        self.assertEqual(zero, "0 s")

    def test_time_to_string_when_time_is_under_60(self):
        seconds = helpers.time_to_string(55)
        self.assertEqual(seconds, "55 s")

    def test_time_to_string_when_time_is_over_60(self):
        minutes = helpers.time_to_string(100)
        self.assertEqual(minutes, "1 m 40 s")
    
    def test_time_to_string_when_time_is_over_3600(self):
        hours = helpers.time_to_string(3610)
        self.assertEqual(hours, "1 h 0 m 10 s")

    def test_time_to_string_when_time_is_over_3660(self):
        hours = helpers.time_to_string(3670)
        self.assertEqual(hours, "1 h 1 m 10 s")