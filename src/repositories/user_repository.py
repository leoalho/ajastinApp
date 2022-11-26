from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def create_user(self, username):
        self._connection.execute(
            """INSERT INTO users (username) values (?)""",[username]
        )

    def all_users(self):
        users = self._connection.execute("SELECT * FROM users").fetchall()
        return users
    
    

user_repository = UserRepository(get_database_connection())