import database

class UserService:

    def __init__(self, connection) -> None:
        self._user = None
        self._project = None
        self._projects = []
        self._connection = connection
        self._users = database.all_users(self._connection)

    def login(self, username):
        for user in self._users:
            if username == user[1]:
                self._user = user
                self.set_projects()
                return True
        return False

    def set_projects(self):
        self._projects = database.user_projects(self._connection, self._user[0])

    def get_projects(self):
        return self._projects

    def get_project(self):
        return self._project

    def set_project(self, project):
        self._project = project

    def get_project_time(self):
        project_time = database.project_time(self._connection, self._project[0])
        return project_time

    def logout(self):
        self._user = None

    def get_user(self):
        return self._user[1]
