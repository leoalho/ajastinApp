from tkinter import ttk, messagebox
import ui.views.project_view as project_view
from ui.views.view_model import View
from sqlite3 import IntegrityError

class NewProject(View):
    """Luokka uuden projektin luomista varten

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
        self._frame = ttk.Frame(master=self._root)
        general_info = ttk.Label(master=self._frame, text="Enter a project name")
        self._entry = ttk.Entry(master=self._frame)
        create_user_button = ttk.Button(master=self._frame,
                            text="create project", command=self._create_project)
        cancel_button = ttk.Button(master=self._frame, text="cancel", command=self._cancel)
        general_info.grid(row=0, column=0, columnspan=2)
        self._entry.grid(row=1, column=0, columnspan=2)
        create_user_button.grid(row=2, column=0)
        cancel_button.grid(row=2, column=1)

    def _create_project(self):
        """Uuden projektin luonnin tapahtumankäsittelijä
        """
        project_name = self._entry.get()
        if project_name != "":
            try:
                self._main_service.create_project(project_name)
                self._mover(project_view.ProjectView(self._root, self._mover, self._main_service))
            except IntegrityError:
                messagebox.showerror('Error', 'Projectname already taken')
    
    def _cancel(self):
        """Palauttaa näkymän takaisin project_view:n
        """
        self._mover(project_view.ProjectView(self._root, self._mover, self._main_service))