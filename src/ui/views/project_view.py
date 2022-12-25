import tkinter as tk
from tkinter import ttk, Menu
from ui.views.main_view import MainView
from ui.views.view_model import View

class ProjectView(View):
    """Luokka päänäkymää varten

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
        self._initialize()
        
    def _initialize(self):
        """Näkymän initialisointi
        """
        self._frame = ttk.Frame(self._root)
        self._menubar()
        userInfo = ttk.Label(master=self._frame, text=f"Logged in as {self._main_service.get_username()}")
        general_info = ttk.Label(master=self._frame, text="Select a project or create a new one")
        projectList = tk.Variable(value = self._main_service.get_project_names())
        self._projects = tk.Listbox(self._frame, listvariable=projectList, height=6, selectmode=tk.SINGLE)
        select_project_button = ttk.Button(master=self._frame, text="Select project", command=self._select_project)
        new_project_button = ttk.Button(master=self._frame, text="New project", command=self._new_project)
        userInfo.grid(row=0,column=0, columnspan=2)
        general_info.grid(row=1, column=0, columnspan=2)
        self._projects.grid(row=2, column=0, columnspan=2)
        select_project_button.grid(row=3, column=0)
        new_project_button.grid(row=3, column=1)
    
    def _menubar(self):
        """Menubarin initialisointi
        """

        menubar = Menu(self._root)
        user_menu = Menu(menubar, tearoff=0)
        help_menu = Menu(menubar, tearoff=0)

        user_menu.add_command(label="Logout", command=self._logout)
        user_menu.add_separator()
        user_menu.add_command(label="Exit", command=self._root.destroy)

        help_menu.add_command(label="Help", command=self._main_service.open_help)

        menubar.add_cascade(label="User", menu=user_menu)
        menubar.add_cascade(label="Help", menu=help_menu)
        self._root.config(menu=menubar)

    def selected_item(self):
        """palauttaa valitun projektin projektikentästä, jos projekteja on olemassa
        """
        if self._projects.size()>0:
            selected = self._projects.curselection()[0]
            return self._projects.get(selected)
        return None

    def _select_project(self):
        """Projektin valinnan tapahtumakäsittelijä. Siirtää käyttäjän main_view:n
        """
        project_name = self.selected_item()
        if project_name:
            self._main_service.set_current_project(project_name)
            self._mover(MainView(self._root, self._mover, self._main_service))
    
    def _new_project(self):
        """Siirtää käyttäjän new_project-view:n"""
        from ui.views.new_project_view import NewProject
        self._mover(NewProject(self._root, self._mover, self._main_service))

    def _logout(self):
        """Kirjautuu ulos ja siirtää käyttäjän login-view:n"""
        self._main_service.logout()
        from ui.views.login_view import LoginView
        self._mover(LoginView(self._root, self._mover, self._main_service))
