from tkinter import ttk, StringVar
import time

class MainView():
    def __init__(self, root, main_service, mover) -> None:
     
        self._root = root
        self._main_service = main_service
        self._mover = mover
        self._frame = None

        self._buttonText = StringVar()
        self._buttonText.set("Start")
        self._timeString = StringVar()
        self._timeString.set(self._main_service.get_current_time())
        self._sumString = StringVar()
        self._sumString.set(f"Total time this session: {self._main_service.get_session_time()}")
        self._projectString = StringVar()
        self._projectString.set(f"""Time spent on current projext: {self._main_service.get_project_time()}""")
        
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        userInfo = ttk.Label(master=self._frame, text=f"Logged in as {self._main_service.get_user()}")
        projectInfo = ttk.Label(master=self._frame, text=f"Working on project {self._main_service.get_project()[1]}")
        Timelabel = ttk.Label(master=self._frame,textvariable=self._timeString)
        button = ttk.Button(master=self._frame, textvariable=self._buttonText, command=self._toggle_timer)
        sumLabel = ttk.Label(master=self._frame, textvariable=self._sumString)
        projectLabel = ttk.Label(master=self._frame, textvariable=self._projectString)
        userInfo.pack()
        projectInfo.pack()
        Timelabel.pack()
        button.pack()
        sumLabel.pack()
        projectLabel.pack()

    def _toggle_timer(self):
        self._main_service.toggle_timer()
        self._sumString.set(f"Total time this session: {self._main_service.get_session_time()}")
        self._timeString.set(self._main_service.get_current_time())
        self._projectString.set(f"""Time spent on current projext: {self._main_service.get_project_time()}""")
        self._buttonText.set("Stop") if self._main_service.get_timer() else self._buttonText.set("Start")
        self.timer()

    def pack(self):
        self._frame.pack()

    def timer(self):
        while self._main_service.get_timer():
            self._timeString.set(self._main_service.tick())
            self._frame.update()
            time.sleep(1)

    def destroy(self):
        self._frame.destroy()
