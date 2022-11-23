from ui.views.mainView import MainView
from ui.views.loginView import LoginView
from services.timer_service import TimerService
from services.user_service import UserService

def initRoot(root): 
    root.geometry("300x250")
    root.resizable(False, False)
    root.title("Timer")


class UI:
    def __init__(self, root, connection):
        self._userService = UserService(connection)
        self._connection = connection
        self._root = root
        self._current_view = LoginView(self._root, self._login, self._userService)

    def start(self):
        self._current_view.pack()

    def _close_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _set_view(self, view):
        self._current_view = view

    def _login(self):
        self._close_current_view()
        self._root.update()
        self._set_view(MainView(self._root, self._userService, self._connection))
        self._current_view.pack()
