from tkinter import ttk, StringVar
import time

class MainView():
    def __init__(self, root, main_service, mover) -> None:
     
        self._root = root
        self._main_service = main_service
        self._user_service = main_service.get_user_service()
        self._timer_service = main_service.get_timer_service()
        self._mover = mover
        self._frame = None

        self._buttonText = StringVar()
        self._buttonText.set("Start")
        self._timeString = StringVar()
        self._timeString.set(self._timer_service.get_current_time())
        self._sumString = StringVar()
        self._sumString.set(f"Total time this session: {self._timer_service.get_session_time()}")
        
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        userInfo = ttk.Label(master=self._frame, text=f"Logged in as {self._user_service.get_user()}")
        projectInfo = ttk.Label(master=self._frame, text=f"Working on project {self._user_service.get_project()}")
        Timelabel = ttk.Label(master=self._frame,textvariable=self._timeString)
        button = ttk.Button(master=self._frame, textvariable=self._buttonText, command=self._toggle_timer)
        sumLabel = ttk.Label(master=self._frame, textvariable=self._sumString)
        projectLabel = ttk.Label(master=self._frame, textvariable=f"Total time spent on project: ")
        userInfo.pack()
        projectInfo.pack()
        Timelabel.pack()
        button.pack()
        sumLabel.pack()

    def _toggle_timer(self):
        self._timer_service.toggle_timer()
        print(self._user_service.get_project_time())
        self._sumString.set(f"Total time this session: {self._timer_service.get_session_time()}")
        self._timeString.set(self._timer_service.get_current_time())
        
        self._buttonText.set("Stop") if self._timer_service.get_timer() else self._buttonText.set("Start")
        print(self._user_service.get_project_time())
        self.timer()

    def pack(self):
        self._frame.pack()

    def timer(self):
        while self._timer_service.get_timer():
            self._timeString.set(self._timer_service.tick())
            self._frame.update()
            time.sleep(1)

    def destroy(self):
        self._frame.destroy()
