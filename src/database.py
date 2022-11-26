import sqlite3
from os.path import exists
from config import DATABASE_FILE_PATH

def connect():
    database = sqlite3.connect(DATABASE_FILE_PATH)
    database.isolation_level = None
    return database

def database_exists():
    return exists(DATABASE_FILE_PATH)

def initialize(database):
    initialize_users(database)
    initialize_projects(database)
    initialize_logs(database)

def initialize_users(database):
    database.execute("DROP TABLE IF EXISTS users;")
    database.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE);")
    database.execute("INSERT INTO users(username) VALUES('Test')")

def initialize_projects(database):
    database.execute("DROP TABLE IF EXISTS projects")
    database.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, projectname TEXT UNIQUE);")
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

def project_sum_time(database, project_id):
    time = database.execute(
        """SELECT SUM(time) FROM logs
        WHERE project_id=?""",[project_id]).fetchone()
    return time

def project_all_times(database, project_id):
    time = database.execute(
        """SELECT * FROM logs
        WHERE project_id=?""",[project_id]).fetchall()
    return time

def new_time(database, project_id, user_id, time):
    database.execute(
        """INSERT INTO logs (project_id, user_id, time)
        VALUES (?,?,?)""",[project_id, user_id, time])
        
def create_user(database, username):
    database.execute(
        """INSERT INTO users (username) values (?)""",[username]
    )

def create_project(database, user_id, project_name):
    cursor=database.cursor()
    cursor.execute("INSERT INTO projects(projectname) VALUES(?)", [project_name])
    project_id = cursor.lastrowid
    cursor.execute("INSERT INTO projectOwners(project_id, user_id) VALUES(?,?)", [project_id, user_id])
    