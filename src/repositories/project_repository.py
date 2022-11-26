from database_connection import get_database_connection

class ProjectRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def user_projects(self, user_id):
        projects = self._connection.execute(
            """SELECT P.id, P.projectname FROM projects P, projectOwners PO
            WHERE P.id=PO.project_id and PO.user_id=?""", [user_id]).fetchall()
        return projects

    def project_sum_time(self, project_id):
        time = self._connection.execute(
            """SELECT SUM(time) FROM logs
            WHERE project_id=?""",[project_id]).fetchone()
        return time

    def create_project(self, user_id, project_name):
        cursor=self._connection.cursor()
        cursor.execute("INSERT INTO projects(projectname) VALUES(?)", [project_name])
        project_id = cursor.lastrowid
        cursor.execute(
            "INSERT INTO projectOwners(project_id, user_id) VALUES(?,?)",
            [project_id, user_id])

    def project_all_times(self, project_id):
        time = self._connection.execute(
            """SELECT * FROM logs
            WHERE project_id=?""",[project_id]).fetchall()
        return time

    def new_time(self, project_id, user_id, time):
        self._connection.execute(
            """INSERT INTO logs (project_id, user_id, time)
            VALUES (?,?,?)""",[project_id, user_id, time])

project_repository = ProjectRepository(get_database_connection())
