from tkinter import ttk, StringVar
from ui.views.projectView import ProjectView

class LoginView():
    def __init__(self, root, mover, main_service) -> None:
        self._root = root
        self._frame = None
        self._mover = mover
        self._main_service = main_service
        self._user_service = main_service.get_user_service()
        self._usernameInput = ""
        self._initialize()
        

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._entry = ttk.Entry(master=self._frame)
        button = ttk.Button(master=self._frame,
                            text="Login", command=self._login)
        self._entry.pack()
        button.pack()

    def _login(self):
        if self._user_service.login(self._entry.get()):
            self._mover(ProjectView(self._root, self._main_service, self._mover))
        else:
            return

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
