from tkinter import ttk, StringVar
import time
from services.timer_service import TimerService


class MainView():
    def __init__(self, root, userService, connection) -> None:
     
        self._root = root
        self._userService = userService
        self._timerService = TimerService(connection)

        self._frame = None
        self._timerOn = False
        self._buttonText = StringVar()
        self._buttonText.set("Start")
        self._timeString = StringVar()
        self._timeString.set(self._timerService.get_current_time())
        self._sumString = StringVar()
        self._sumString.set(f"Total time this session: {self._timerService.get_total_time()}")
        
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        userInfo = ttk.Label(master=self._frame,
                             text=f"Logged in as {self._userService.get_user()}")
        Timelabel = ttk.Label(master=self._frame,
                              textvariable=self._timeString)
        button = ttk.Button(
            master=self._frame, textvariable=self._buttonText, command=self._toggle_timer)
        sumLabel = ttk.Label(master=self._frame, textvariable=self._sumString)
        userInfo.pack()
        Timelabel.pack()
        button.pack()
        sumLabel.pack()

    def _toggle_timer(self):
        if self._timerOn:
            self._timerService.reset()
            self._sumString.set(f"Total time this session: {self._timerService.get_total_time()}")
            self._timeString.set(self._timerService.get_current_time())
        self._timerOn = not self._timerOn
        self._buttonText.set("Stop") if self._timerOn else self._buttonText.set("Start")
        self.timer()

    def pack(self):
        self._frame.pack()

    def timer(self):
        while self._timerOn:
            self._timeString.set(self._timerService.tick())
            self._frame.update()
            time.sleep(1)

    def destroy(self):
        self._frame.destroy()
