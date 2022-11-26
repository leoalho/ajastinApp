import tkinter as tk
from tkinter import ttk
from ui.views.mainView import MainView

class ProjectView():
    def __init__(self, root, mover, main_service) -> None:
        self._root = root
        self._frame = None
        self._main_service = main_service
        self._mover = mover
        self._initialize()
        
    def _initialize(self):
        self._frame = ttk.Frame(self._root)
        userInfo = ttk.Label(master=self._frame, text=f"Logged in as {self._main_service.get_user()}")
        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._logout)
        general_info = ttk.Label(master=self._frame, text="Select a project or create a new one")
        projectList = tk.Variable(value = self._main_service.get_projects())
        self._projects = tk.Listbox(self._frame, listvariable=projectList, height=6, selectmode=tk.SINGLE)
        select_project_button = ttk.Button(master=self._frame, text="Select project", command=self._select_project)
        new_project_button = ttk.Button(master=self._frame, text="New project", command=self._new_project)
        userInfo.grid(row=0,column=0)
        logout_button.grid(row=0, column=1)
        general_info.grid(row=1, column=0, columnspan=2)
        self._projects.grid(row=2, column=0, columnspan=2)
        select_project_button.grid(row=3, column=0)
        new_project_button.grid(row=3, column=1)
    
    def selected_item(self):
        selected = self._projects.curselection()[0]
        return self._projects.get(selected)
           
    def _select_project(self):
        project = self.selected_item()
        if project:
            self._main_service.set_project(project)
            self._mover(MainView(self._root, self._mover, self._main_service))
    
    def _new_project(self):
        from ui.views.new_project_view import NewProject
        self._mover(NewProject(self._root, self._mover, self._main_service))

    def _logout(self):
        self._main_service.logout()
        from ui.views.loginView import LoginView
        self._mover(LoginView(self._root, self._mover, self._main_service))

    def pack(self):
        self._frame.pack()
    
    def destroy(self):
        self._frame.destroy()