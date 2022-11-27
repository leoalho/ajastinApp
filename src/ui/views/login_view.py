from tkinter import ttk
import ui.views.project_view as project_view
import ui.views.new_user_view as new_user_view

class LoginView():
    def __init__(self, root, mover, main_service) -> None:
        self._root = root
        self._frame = None
        self._mover = mover
        self._main_service = main_service
        self._usernameInput = ""
        self._initialize()
        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        general_info = ttk.Label(master=self._frame, text="Login")
        username = ttk.Label(master=self._frame, text="Username: ")
        self._entry = ttk.Entry(master=self._frame)
        login_button = ttk.Button(master=self._frame,
                            text="Login", command=self._login)
        new_user_button = ttk.Button(master=self._frame,
                            text="create new user", command=self._create_user)
        general_info.grid(row=0, column=0, columnspan=3)
        username.grid(row=1, column=0)
        self._entry.grid(row=1, column=1, columnspan=2)
        login_button.grid(row=2, column=0)
        new_user_button.grid(row=2, column=1)

    def _login(self):
        if self._main_service.login(self._entry.get()):
            self._mover(project_view.ProjectView(self._root, self._mover, self._main_service))
        else:
            return

    def _create_user(self):
        self._mover(new_user_view.NewUser(self._root, self._mover, self._main_service))

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
