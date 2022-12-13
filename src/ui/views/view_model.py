from tkinter import ttk
class View:
    """Näkymäluokka, jonka muut luokat perivät
    """
    def __init__(self, root, mover, main_service) -> None:
        """Luokan konstruktori

        Args:
            root: Näkymän juuri
            mover: Metodi näkymän vaihtamista varten
            main_service: Toiminnallisuutta varten
        """
        self._root = root
        self._root.config(menu="")
        self._frame = None
        self._mover = mover
        self._main_service = main_service

    def pack(self):
        """Pakkaa näkymän"""
        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()
