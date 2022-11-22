from tkinter import ttk, StringVar
import time
#from services.timer_service import timer_service

class MainView():
  def __init__(self, root) -> None:
    self._root = root
    self._frame = None
    self._timerOn = False
    self._buttonText = StringVar()
    self._buttonText.set("Start")
    self._time = 0
    self._timeString = StringVar()
    self._timeString.set(self._time)
    self._initialize()

  def _initialize(self):
    self._frame = ttk.Frame(master=self._root)
    label = ttk.Label(master=self._frame, textvariable=self._timeString)
    button = ttk.Button(master=self._frame, textvariable=self._buttonText, command=self._toggle_timer)
    label.pack()
    button.pack()

  def _toggle_timer(self):
    self._timerOn = not self._timerOn
    self._buttonText.set("Stop") if self._timerOn else self._buttonText.set("Start")
    self.timer()

  def pack(self):
    self._frame.pack()

  def timer(self):
    while self._timerOn:
      self._time += 1
      self._timeString.set(self._time)
      self._frame.update()
      time.sleep(1)

