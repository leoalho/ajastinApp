from services.timer_service import TimerService
from services.user_service import UserService

class MainService():
    def __init__(self, connection) -> None:
        self._connection = connection
        self._user_service = UserService(self._connection)
        self._timer_service = TimerService(self._connection)

    def get_user_service(self):
        return self._user_service

    def get_timer_service(self):
        return self._timer_service
