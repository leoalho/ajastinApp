from tkinter import ttk, StringVar
import time
import ui.views.login_view as login_view
import ui.views.project_view as project_view
from ui.views.view_model import View

class MainView(View):
    def __init__(self, root, mover, main_service) -> None:
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
        self._frame = ttk.Frame(master=self._root)
        userInfo = ttk.Label(master=self._frame, text=f"Logged in as {self._main_service.get_username()}")
        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._logout)
        project_info = ttk.Label(master=self._frame, text=f"Working on project {self._main_service.get_current_project().name}")
        project_button = ttk.Button(master=self._frame, text="change project", command=self._change_project)
        time_label = ttk.Label(master=self._frame,textvariable=self._timeString)
        timer_button = ttk.Button(master=self._frame, textvariable=self._buttonText, command=self._toggle_timer)
        sum_label = ttk.Label(master=self._frame, textvariable=self._sumString)
        project_label = ttk.Label(master=self._frame, textvariable=self._projectString)
        times_per_day_label = ttk.Label(master=self._frame, textvariable=self._last_days)
        export_button = ttk.Button(master=self._frame, text="Export as .txt", command=self._export)
        
        userInfo.grid(row=0, column=0)
        logout_button.grid(row=0, column=1)
        project_info.grid(row=1, column=0)
        project_button.grid(row=1, column=1)
        time_label.grid(row=2, column=0)
        timer_button.grid(row=2, column=1)
        sum_label.grid(row=3, column=0, columnspan=2)
        project_label.grid(row=4, column=0, columnspan=2)
        times_per_day_label.grid(row=5, column=0, columnspan=2)
        export_button.grid(row=6, column=0)

    def _toggle_timer(self):
        self._main_service.toggle_timer()
        self._sumString.set(f"Total time this session: {self._main_service.get_session_time()}")
        self._timeString.set(self._main_service.get_current_time())
        self._projectString.set(f"""Time spent on current projext: {self._main_service.get_project_time()}""")
        self._buttonText.set("Stop") if self._main_service.get_timer() else self._buttonText.set("Start")
        self._last_days.set(self._main_service.get_time_per_day())
        self.timer()

    def _logout(self):
        self._main_service.logout()    
        self._mover(login_view.LoginView(self._root, self._mover, self._main_service))

    def _change_project(self):
        self._main_service.close_project()
        self._mover(project_view.ProjectView(self._root, self._mover, self._main_service))
    
    def _export(self):
        self._main_service.export()

    def timer(self):
        while self._main_service.get_timer():
            self._timeString.set(self._main_service.tick())
            self._frame.update()
            time.sleep(1)
