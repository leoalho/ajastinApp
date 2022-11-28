from tkinter import ttk
class View:
    def __init__(self, root, mover, main_service) -> None:
        self._root = root
        self._frame = None
        self._mover = mover
        self._main_service = main_service

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
