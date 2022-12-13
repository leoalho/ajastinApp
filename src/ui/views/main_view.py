from tkinter import ttk, StringVar, Menu, messagebox
import time
import ui.views.login_view as login_view
import ui.views.project_view as project_view
from ui.views.view_model import View

class MainView(View):
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

        self._buttonText = StringVar()
        self._buttonText.set("Start")
        self._timeString = StringVar()
        self._timeString.set(self._main_service.get_current_time())
        self._sumString = StringVar()
        self._sumString.set(f"Total time this session: {self._main_service.get_session_time()}")
        self._projectString = StringVar()
        self._projectString.set(f"""Time spent on current projext: {self._main_service.get_project_time()}""")
        self._last_days  = StringVar()
        self._last_days.set(self._main_service.get_time_per_day())
        
        self._initialize()

    def _initialize(self):
        """Näkymän initialisointi
        """

        self._frame = ttk.Frame(master=self._root)
        self._menubar()
        info_label = ttk.Label(master=self._frame,
            text=f"Logged in as {self._main_service.get_username()}, Working on project {self._main_service.get_current_project().name}")
        time_label = ttk.Label(master=self._frame,textvariable=self._timeString, font=("Arial", 25))
        timer_button = ttk.Button(master=self._frame, textvariable=self._buttonText, command=self._toggle_timer)
        sum_label = ttk.Label(master=self._frame, textvariable=self._sumString)
        project_label = ttk.Label(master=self._frame, textvariable=self._projectString)
        times_per_day_label = ttk.Label(master=self._frame, textvariable=self._last_days)
        
        info_label.grid(row=0, column=0)
        time_label.grid(row=1, column=0)
        timer_button.grid(row=2, column=0)
        sum_label.grid(row=3, column=0)
        project_label.grid(row=4, column=0)
        times_per_day_label.grid(row=5, column=0)

    def _menubar(self):
        """menubarin initialisointi
        """

        menubar = Menu(self._root)
        user_menu = Menu(menubar, tearoff=0)
        project_menu = Menu(menubar, tearoff=0)
        export_menu = Menu(project_menu, tearoff=0)

        user_menu.add_command(label="Logout", command=self._logout)
        user_menu.add_separator()
        user_menu.add_command(label="Exit", command=self._root.destroy)

        export_menu.add_command(label='.txt', command=self._export_txt)
        export_menu.add_command(label='.pdf', command=self._export_pdf)
        
        project_menu.add_cascade(label="Export as...", menu=export_menu)
        project_menu.add_command(label="Close", command=self._change_project)

        menubar.add_cascade(label="User", menu=user_menu)
        menubar.add_cascade(label="Project", menu=project_menu)
        self._root.config(menu=menubar)

    def _toggle_timer(self):
        """Start/stop-painikkeen tapahtumankäsittelijä
        """

        self._main_service.toggle_timer()
        self._sumString.set(f"Total time this session: {self._main_service.get_session_time()}")
        self._timeString.set(self._main_service.get_current_time())
        self._projectString.set(f"""Time spent on current projext: {self._main_service.get_project_time()}""")
        self._buttonText.set("Stop") if self._main_service.get_timer() else self._buttonText.set("Start")
        self._last_days.set(self._main_service.get_time_per_day())
        self.timer()

    def _logout(self):
        """Uloskirjautumisen tapahtumankäsittelijä, siirtää käyttäjän takaisin login_view-näkymään
        """

        self._main_service.logout()    
        self._mover(login_view.LoginView(self._root, self._mover, self._main_service))

    def _change_project(self):
        """Projektin vaihtamisen tapahtumankäsittelijä, siitää käyttäjän project_view-näkymään
        """
        self._main_service.close_project()
        self._mover(project_view.ProjectView(self._root, self._mover, self._main_service))
    
    def _export_txt(self):
        """.txt-tiedostojen eksporttauksesta vastaava tapahtumankäsittelijä"""
        filename = self._main_service.export("txt")
        messagebox.showinfo("File created", f"Created file {filename}")

    def _export_pdf(self):
        """.pdf-tiedostojen eksporttauksesta vastaava tapahtumankäsittelijä"""
        filename = self._main_service.export("pdf")
        messagebox.showinfo("File created", f"Created file {filename}")

    def timer(self):
        """Looppi, joka päivittää timeria sekunnin välein niin kauan kun timer on päällä
        """
        while self._main_service.get_timer():
            self._timeString.set(self._main_service.tick())
            self._frame.update()
            time.sleep(1)
