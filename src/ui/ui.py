from ui.views.loginView import LoginView
from services.main_service  import MainService

def initRoot(root): 
    root.geometry("640x480")
    root.resizable(False, False)
    root.title("Timer")

class UI:
    def __init__(self, root):
        self._main_service = MainService()
        self._current_view = LoginView(root, self._mover, self._main_service)

    def start(self):
        self._current_view.pack()

    def _close_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _set_view(self, view):
        self._current_view = view

    def _mover(self, view):
        self._close_current_view()
        self._set_view(view)
        self._current_view.pack()