import sqlite3
from config import DATABASE_FILE_PATH

def connect():
    database = sqlite3.connect(DATABASE_FILE_PATH)
    database.isolation_level = None
    return database

def initialize(database):
    initialize_users(database)
    initialize_projects(database)
    initialize_logs(database)

def initialize_users(database):
    database.execute("DROP TABLE IF EXISTS users;")
    database.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT);")
    database.execute("INSERT INTO users(username) VALUES('Test')")

def initialize_projects(database):
    database.execute("DROP TABLE IF EXISTS projects")
    database.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, projectname TEXT);")
    database.execute("INSERT INTO projects(projectname) VALUES('TestProject')")
    database.execute("DROP TABLE IF EXISTS projectOwners")
    database.execute(
        "CREATE TABLE projectOwners (project_id REFERENCES projects, user_id references users)")
    database.execute("INSERT INTO projectOwners(project_id, user_id) VALUES(1,1)")

def initialize_logs(database):
    database.execute("DROP TABLE IF EXISTS logs")
    database.execute(
        """CREATE TABLE logs (
        id INTEGER PRIMARY KEY,
        project_id REFERENCES projects,
        user_id references users,
        time INTEGER )""")

def all_users(database):
    users = database.execute("SELECT * FROM users").fetchall()
    return users

def user_projects(database, user_id):
    projects = database.execute(
        """SELECT P.id, P.projectname FROM projects P, projectOwners PO
         WHERE P.id=PO.project_id and PO.user_id=?""", [user_id]).fetchall()
    return projects

def project_time(database, project_id):
    time = database.execute(
        """SELECT SUM(time) FROM logs
        WHERE project_id=?""",[project_id]).fetchone()
    return time
