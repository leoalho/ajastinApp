import database

class UserService:

    def __init__(self, connection) -> None:
        self._user = None
        self._connection = connection
        database.initialize_users(self._connection)
        self._users = database.all_users(self._connection)

    def login(self, username):
        for user in self._users:
            if username == user[1]:
                self._user = user
                return True
        return False

    def logout(self):
        self._user = None

    def get_user(self):
        return self._user[1]
