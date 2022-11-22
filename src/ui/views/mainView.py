from tkinter import ttk, StringVar
import time
#from services.timer_service import timer_service

class MainView():
  def __init__(self, root, timerService) -> None:
    self._root = root
    self._frame = None
    self._timerOn = False
    self._buttonText = StringVar()
    self._buttonText.set("Start")
    self._time = 0
    self._sum = 0
    self._timeString = StringVar()
    self._timeString.set(f"{self._time} s")
    self._sumString = StringVar()
    self._sumString.set(f"Total time this session: {self._sum} s")
    self._timerService = timerService
    self._initialize()

  def _initialize(self):
    self._frame = ttk.Frame(master=self._root)
    userInfo = ttk.Label(master=self._frame, text=f"Logged in as {self._timerService.user[1]}")
    Timelabel = ttk.Label(master=self._frame, textvariable=self._timeString)
    button = ttk.Button(master=self._frame, textvariable=self._buttonText, command=self._toggle_timer)
    sumLabel = ttk.Label(master=self._frame,textvariable=self._sumString)
    userInfo.pack()
    Timelabel.pack()
    button.pack()
    sumLabel.pack()

  def _toggle_timer(self):
    if self._timerOn:
      self._sum += self._time
      self._sumString.set(f"Total time this session: {self._sum} s")
      self._time = 0
      self._timeString.set(0)
    self._timerOn = not self._timerOn
    self._buttonText.set("Stop") if self._timerOn else self._buttonText.set("Start")
    self.timer()

  def pack(self):
    self._frame.pack()

  def timer(self):
    while self._timerOn:
      self._time += 1
      self._timeString.set(f"{self._time} s")
      self._frame.update()
      time.sleep(1)

  def destroy(self):
      self._frame.destroy()
