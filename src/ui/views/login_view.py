from tkinter import ttk, messagebox
import ui.views.project_view as project_view
import ui.views.new_user_view as new_user_view
from ui.views.view_model import View

class LoginView(View):
    """Luokka kirjautumisnäkymää varten

    Args:
        View: Luokka perii luokan view_model
    """

    def __init__(self, root, mover, main_service) -> None:
        """Luokan konstruktori

        Args:
            root: Näkymän juuri
            mover: Metodi näkymän vaihtamista varten
            main_service: Toiminnallisuutta varten
        """

        super().__init__(root, mover, main_service)
        self._usernameInput = ""
        self._initialize()
        
    def _initialize(self):
        """Näkymän initialisointi
        """

        self._frame = ttk.Frame(master=self._root)
        general_info = ttk.Label(master=self._frame, text="Login")
        username_label = ttk.Label(master=self._frame, text="Username: ")
        self._username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame,text="Password: ")
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        login_button = ttk.Button(master=self._frame,
                            text="Login", command=self._login)
        new_user_button = ttk.Button(master=self._frame,
                            text="create new user", command=self._create_user)
        general_info.grid(row=0, column=0, columnspan=3)
        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1, columnspan=2)
        password_label.grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1, columnspan=2)
        login_button.grid(row=3, column=0)
        new_user_button.grid(row=3, column=1)

    def _login(self):
        """Sisäänkirjautumispainikkeen tapahtumankäsittelijä,
        jos kirjautuminen onnistuu, siirtyy project_view-näkymään,
        muutoin antaa virheilmoituksen
        """

        if self._main_service.login(self._username_entry.get(), self._password_entry.get()):
            self._mover(project_view.ProjectView(self._root, self._mover, self._main_service))
        else:
            messagebox.showerror('Error', 'Incorrect username/password')

    def _create_user(self):
        """Tapahtumankäsittelijä create_user painikkeelle, siirtyy new_user-näkymään
        """

        self._mover(new_user_view.NewUser(self._root, self._mover, self._main_service))
