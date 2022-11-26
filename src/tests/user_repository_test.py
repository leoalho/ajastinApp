import unittest
from repositories.user_repository import UserRepository
from initialize_database import initialize
from database_connection import get_database_connection

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize()
        self.connection = get_database_connection()
        self.user_repository = UserRepository(self.connection)

    def test_one_user_at_initialization(self):
        users = self.user_repository.all_users()
        self.assertEqual(len(users), 1)
    
    def test_creating_user_adds_a_new_user(self):
        self.user_repository.create_user("Tester")
        users = self.user_repository.all_users()
        self.addClassCleanup(len(users), 2)