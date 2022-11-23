#from entities.user import User
import database

class TimerService:

    def __init__(self) -> None:
        self.user = None
        self.connection = database.connect()
        database.initialize_users(self.connection)
        self.users = database.all_users(self.connection)

    def login(self, username):
        for user in self.users:
            if username == user[1]:
                self.user = user
                return True
        return False

    def logout(self):
        self.user = None
