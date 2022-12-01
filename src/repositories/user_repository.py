from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def create_user(self, username, password):
        self._connection.execute(
            """INSERT INTO users (username, password) values (?,?)""",[username,password]
        )

    def all_users(self):
        users = self._connection.execute("SELECT * FROM users").fetchall()
        return users

    def get_user(self, username):
        user = self._connection.execute(
            "SELECT * FROM users WHERE username=?",[username]).fetchone()
        return user

user_repository = UserRepository(get_database_connection())
