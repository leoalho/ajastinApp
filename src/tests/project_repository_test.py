import unittest
from datetime import datetime
from repositories.project_repository import ProjectRepository
from repositories.user_repository import UserRepository
from initialize_database import initialize
from database_connection import get_database_connection

class TestProjectRepository(unittest.TestCase):
    def setUp(self):
        initialize()
        self.connection = get_database_connection()
        self.user_repository = UserRepository(self.connection)
        self.project_repository = ProjectRepository(self.connection)
        self.user_id = self.connection.execute(
            """SELECT id FROM users where username='Test'""").fetchone()[0]
        print(self.user_id)

    def test_user_has_one_project_at_initialization(self):
        projects = self.project_repository.user_projects(self.user_id)
        self.assertEqual(len(projects),1)

    def test_creating_a_project_adds_a_project(self):
        self.project_repository.create_project(self.user_id,"Testiprojekti")
        projects = self.project_repository.user_projects(self.user_id)
        self.assertEqual(len(projects),2)

    def test_new_time_adds_a_time(self):
        projects = self.project_repository.user_projects(self.user_id)
        project_id = projects[0][0]
        time1 = datetime.now()
        time2 = datetime.now()
        self.project_repository.new_time(self.user_id, project_id, 10, time1, time2)
        all_times = self.project_repository.time_per_day(project_id)
        self.assertEqual(len(all_times), 1)