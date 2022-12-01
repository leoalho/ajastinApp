import unittest
from repositories.project_repository import ProjectRepository
from initialize_database import initialize
from database_connection import get_database_connection

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize()
        self.connection = get_database_connection()
        self.user_repository = ProjectRepository(self.connection)
        self.user_id = self.connection

    def test_one_user_at_initialization(self):
        users = self.user_repository.all_users()
        self.assertEqual(len(users), 1)
    
    def test_creating_user_adds_a_new_user(self):
        self.user_repository.create_user("Tester")
        users = self.user_repository.all_users()
        self.assertEqual(len(users), 2)