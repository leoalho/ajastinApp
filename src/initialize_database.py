from database_connection import get_database_connection

def initialize():
    """Initialisoi tietokannan

    Args:
        database: tietokantaliittymä
    """

    database = get_database_connection()
    initialize_users(database)
    initialize_projects(database)
    initialize_logs(database)

def initialize_users(database):
    """Luo taulukot käyttäjiä varten, sekä luo default-käyttäjän

    Args:
        database: tietokantaliittymä
    """

    database.execute("DROP TABLE IF EXISTS users;")
    database.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT);")
    database.execute("""INSERT INTO users(username, password)
         VALUES('Test', '$2b$12$DJ0dBrcRB.Vd3YPVh6CdX.8qaa9hbYckb4q1NAh9FSOwgW7Kx/BEm')""")

def initialize_projects(database):
    """Luo taulukot projekteja varten sekä luo default projektin

    Args:
        database: tietokantaliittymä
    """

    database.execute("DROP TABLE IF EXISTS projects")
    database.execute("CREATE TABLE projects (id INTEGER PRIMARY KEY, projectname TEXT UNIQUE);")
    database.execute("INSERT INTO projects(projectname) VALUES('TestProject')")
    database.execute("DROP TABLE IF EXISTS projectOwners")
    database.execute(
        "CREATE TABLE projectOwners (project_id REFERENCES projects, user_id references users)")
    database.execute("INSERT INTO projectOwners(project_id, user_id) VALUES(1,1)")

def initialize_logs(database):
    """Luo taulukot ajanottoa varten

    Args:
        database: tietokantaliittymä
    """

    database.execute("DROP TABLE IF EXISTS logs")
    database.execute(
        """CREATE TABLE logs (
        id INTEGER PRIMARY KEY,
        project_id REFERENCES projects,
        user_id references users,
        time INTEGER,
        startTime timestamp,
        endTime timestamp )""")
