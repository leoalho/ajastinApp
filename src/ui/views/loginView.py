from tkinter import ttk, StringVar

class LoginView():
    def __init__(self, root, login, timerService) -> None:
        self._root = root
        self._usernameInput = ""
        self._frame = None
        self._timerService = timerService
        self._initialize()
        self._loginService = login
      
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._entry = ttk.Entry(master=self._frame)
        button = ttk.Button(master=self._frame, text="Login", command=self._login)
        self._entry.pack()
        button.pack()
    
    def _login(self):
      if self._timerService.login(self._entry.get()):
          self._loginService()
      else:
          return

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()