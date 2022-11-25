import database
import helpers

class MainService():
    def __init__(self, connection) -> None:
        self._user = None
        self._project = None
        self._projects = []
        self._connection = connection
        self._users = database.all_users(self._connection)
        self._current_time = 0
        self._session_time = 0
        self._timer = False

    def login(self, username):
        for user in self._users:
            if username == user[1]:
                self._user = user
                #self.set_projects()
                return True
        return False

    def set_projects(self):
        self._projects = database.user_projects(self._connection, self._user[0])

    def get_projects(self):
        #return self._projects
        return database.user_projects(self._connection, self._user[0])

    def get_project(self):
        return self._project

    def set_project(self, project):
        self._project = project

    def get_project_time(self):
        project_time = database.project_sum_time(self._connection, self._project[0])
        return helpers.time_to_string(project_time[0])

    def logout(self):
        self._user = None

    def get_user(self):
        return self._user[1]

    def tick(self):
        self._current_time += 1
        return helpers.time_to_string(self._current_time)

    def reset(self):
        self._session_time += self._current_time
        database.new_time(self._connection, self._project[0], self._user[0], self._current_time)
        self._current_time = 0
        
    def toggle_timer(self):
        if not self._timer:
            self._timer = True
        else:
            self._timer = False
            self.reset()

    def get_timer(self):
        return self._timer

    def get_current_time(self):
        return helpers.time_to_string(self._current_time)

    def get_session_time(self):
        return helpers.time_to_string(self._session_time)
