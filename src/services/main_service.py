import os
from datetime import datetime
from repositories.project_repository import project_repository
from repositories.user_repository import user_repository
from entities.timer import Timer
from entities.user import User
from entities.project import Project
from config import EXPORT_DIRECTORY
import helpers

class MainService():
    def __init__(self) -> None:
        self._user = None
        self._timer = Timer()

    def login(self, username, password):
        user = user_repository.get_user(username)
        if user and helpers.validate_password(password, user):
            self._user = User(user[0], user[1])
            self.set_projects()
            return True
        return False

    def logout(self):
        self.close_project()
        self._user = None

    def set_projects(self):
        projects = project_repository.user_projects(self._user.db_id)
        self._user.projects = []
        for project in projects:
            self._user.projects.append(Project(project[0], project[1]))

    def get_projects(self):
        return self._user.projects

    def get_project_names(self):
        projects = self.get_projects()
        names = map(lambda x: x.name, projects)
        return list(names)

    def get_current_project(self):
        return self._user.current_project

    def set_current_project(self, project_name):
        for project in self._user.projects:
            if project.name == project_name:
                self._user.current_project = project

    def get_username(self):
        if self._user:
            return self._user.username
        return None

    def tick(self):
        return self._timer.tick()

    def close_project(self):
        self._timer.reset()
        self._timer.session_time = 0
        self._user.current_project = None

    def reset(self):
        startstop = self._timer.get_start_stop()
        new_time = self._timer.reset()
        project_repository.new_time(
            self._user.current_project.db_id,
            self._user.db_id, new_time, startstop[0], startstop[1])

    def toggle_timer(self):
        self._timer.toggle_timer()
        if not self._timer.timer_on:
            self.reset()

    def get_timer(self):
        return self._timer.timer_on

    def get_current_time(self):
        return self._timer.current_time

    def get_session_time(self):
        return self._timer.session_time

    def get_project_time(self):
        project_time = project_repository.project_sum_time(self._user.current_project.db_id)
        return helpers.time_to_string(project_time[0])

    def get_time_per_day(self):
        times = project_repository.time_per_day(self._user.current_project.db_id)
        result = "TIme spent on project during last days:\n"
        for time in times:
            result += f"{time[0]}: {helpers.time_to_string(time[1])} \n"
        return result

    def export(self):
        now = datetime.now()

        times = project_repository.time_per_day(self._user.current_project.db_id)

        textbody = f"""Daily log of
         {self._user.username} on project {self._user.current_project.name}:\n"""
        for time in times:
            textbody += f"{time[0]}: {helpers.time_to_string(time[1])} \n"
        textbody += "------------------\n"
        textbody += f"Time in total: {self.get_project_time()}"
        date = now.strftime('%Y%m%d')

        filename =f"{date}{self._user.current_project.name}.txt"
        filepath = os.path.join(EXPORT_DIRECTORY,filename)
        with open(filepath, "w", encoding="utf8") as file:
            file.write(textbody)

    def create_user(self, username, password):
        hashed_password = helpers.hash_password(password)

        user_repository.create_user(username, hashed_password)

    def create_project(self, project_name):
        project_repository.create_project(self._user.db_id, project_name)
        self.set_projects()
