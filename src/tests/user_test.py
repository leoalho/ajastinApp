import unittest
from entities.user import User


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.user = User("Testman", "secret")

    def test_user_initializes_with_right_values(self):
        self.assertEqual(self.user.username, "Testman")
        self.assertEqual(self.user.password, "secret")
