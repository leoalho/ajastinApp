from ui.views.mainView import MainView
from ui.views.loginView import LoginView
from services.timer_service import TimerService

class UI:
    def __init__(self, root):
        self._timerService = TimerService()
        self._root = root
        self._current_view = LoginView(self._root, self._login, self._timerService)

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
        self._set_view(MainView(self._root, self._timerService))
        self._current_view.pack()