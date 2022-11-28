from tkinter import ttk
import ui.views.login_view as login_view
from ui.views.view_model import View

class NewUser(View):
    def __init__(self, root, mover, main_service) -> None:
        super().__init__(root, mover, main_service)
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        general_info = ttk.Label(master=self._frame, text="Enter a new username")
        self._entry = ttk.Entry(master=self._frame)
        create_user_button = ttk.Button(master=self._frame,
                            text="Create user", command=self._create_user)
        cancel_button = ttk.Button(master=self._frame,
                            text="cancel", command=self._cancel)
        general_info.grid(row=0,column=0, columnspan=2)
        self._entry.grid(row=1,column=0, columnspan=2)
        create_user_button.grid(row=2, column=0)
        cancel_button.grid(row=2, column=1)

    def _create_user(self):
        username = self._entry.get()
        if username != "":
            self._main_service.create_user(username)
            self._mover(login_view.LoginView(self._root, self._mover, self._main_service))
    
    def _cancel(self):
        self._mover(login_view.LoginView(self._root, self._mover, self._main_service))