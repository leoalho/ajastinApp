from tkinter import ttk, messagebox
import ui.views.login_view as login_view
from ui.views.view_model import View
from sqlite3 import IntegrityError

class NewUser(View):
    def __init__(self, root, mover, main_service) -> None:
        super().__init__(root, mover, main_service)
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        general_info = ttk.Label(master=self._frame, text="Create a new username")
        username_label = ttk.Label(master=self._frame, text="Username: ")
        self._username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text="Password: ")
        self._password_entry = self._entry = ttk.Entry(master=self._frame, show="*")
        password_label2 = ttk.Label(master=self._frame, text="Password again: ")
        self._password_entry2 = self._entry = ttk.Entry(master=self._frame, show="*")
        create_user_button = ttk.Button(master=self._frame,
                            text="Create user", command=self._create_user)
        cancel_button = ttk.Button(master=self._frame,
                            text="cancel", command=self._cancel)
        general_info.grid(row=0,column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1,column=1, columnspan=2)
        password_label.grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1, columnspan=2)
        password_label2.grid(row=3, column=0)
        self._password_entry2.grid(row=3, column=1, columnspan=2)
        create_user_button.grid(row=4, column=0)
        cancel_button.grid(row=4, column=1)

    def _create_user(self):
        username = self._username_entry.get()
        if username != "":
            if self._password_entry.get() != self._password_entry2.get():
                messagebox.showerror('Error', 'Passwords do not match')
                return
            try:
                self._main_service.create_user(username, self._password_entry.get())
                self._mover(login_view.LoginView(self._root, self._mover, self._main_service))
            except IntegrityError:
                messagebox.showerror('Error', 'Username already taken')
    
    def _cancel(self):
        self._mover(login_view.LoginView(self._root, self._mover, self._main_service))