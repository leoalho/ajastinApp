from repositories.project_repository import project_repository
from repositories.user_repository import user_repository
from entities.timer import Timer
import helpers

class MainService():
    def __init__(self) -> None:
        self._user = None
        self._project = None
        self._projects = []
        self.timer = Timer()

    def login(self, username):
        users = user_repository.all_users()
        for user in users:
            if username == user[1]:
                self._user = user
                #self.set_projects()
                return True
        return False

    def set_projects(self):
        self._projects = project_repository.user_projects(self._user[0])

    def get_projects(self):
        return project_repository.user_projects(self._user[0])

    def get_project_names(self):
        projects = self.get_projects()
        names = map(lambda x: x[1], projects)
        return list(names)

    def get_project(self):
        return self._project

    def set_project(self, project):
        self._project = project

    def logout(self):
        self._user = None
        self.close_project()

    def close_project(self):
        self._project = None

    def get_user(self):
        return self._user[1]

    def tick(self):
        return self.timer.tick()

    def reset(self):
        new_time = self.timer.reset()
        project_repository.new_time(self._project[0], self._user[0], new_time)

    def toggle_timer(self):
        self.timer.toggle_timer()
        if not self.timer.get_timer():
            self.reset()

    def get_timer(self):
        return self.timer.get_timer()

    def get_current_time(self):
        return self.timer.get_current_time()

    def get_session_time(self):
        return self.timer.get_session_time()

    def get_project_time(self):
        project_time = project_repository.project_sum_time(self._project[0])
        return helpers.time_to_string(project_time[0])

    def create_user(self, username):
        user_repository.create_user(username)

    def create_project(self, project_name):
        project_repository.create_project(self._user[0], project_name)
