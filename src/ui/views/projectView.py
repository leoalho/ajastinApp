import tkinter as tk
from tkinter import ttk
from ui.views.mainView import MainView

class ProjectView():
    def __init__(self, root, main_service, mover) -> None:
        self._root = root
        self._frame = None
        self._main_service = main_service
        self._mover = mover
        self._initialize()
        
    def _initialize(self):
        self._frame = ttk.Frame(self._root)
        userInfo = ttk.Label(master=self._frame, text=f"Logged in as {self._main_service.get_user()}")
        generalInfo = ttk.Label(master=self._frame, text="Select a project or create a new one")
        projectList = tk.Variable(value = self._main_service.get_projects())
        self._projects = tk.Listbox(self._frame, listvariable=projectList, height=6, selectmode=tk.SINGLE)
        select_project_button = ttk.Button(master=self._frame, text="Select project", command=self._select_project)
        new_project_button = ttk.Button(master=self._frame, text="New project", command=self.selected_item)
        userInfo.pack()
        generalInfo.pack()
        self._projects.pack()
        select_project_button.pack()
        new_project_button.pack()
    
    def selected_item(self):
        selected = self._projects.curselection()[0]
        return self._projects.get(selected)
           
    def _select_project(self):
        project = self.selected_item()
        if project:
            self._main_service.set_project(project)
            self._mover(MainView(self._root, self._main_service, self._mover))
    
    def _new_project(self):
        return

    def pack(self):
        self._frame.pack()
    
    def destroy(self):
        self._frame.destroy()