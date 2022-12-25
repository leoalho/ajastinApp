from ui.views.login_view import LoginView
from services.main_service  import MainService

def initRoot(root): 
    """Käyttöliittymän ruudun initialisointi

    Args:
        root: Tk-olio
    """

    root.geometry("480x480")
    root.resizable(False, False)
    root.title("Timer")

class UI:
    """Käyttöliittymän pääluokka
    """

    def __init__(self, root):
        """Luokan konstruktori. Liittää mainservice-olion käyttöliittymään, sekä luo alkunäkymän (LoginView)

        Args:
            root: Tk-olio
        """

        self._main_service = MainService()
        self._current_view = LoginView(root, self._mover, self._main_service)

    def start(self):
        """Paketoi kyseisen näkymän"""

        self._current_view.pack()

    def _close_current_view(self):
        """Sulkee kyseisen näkymän"""

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _set_view(self, view):
        """Asettaa uuden näkymän nykynäkymäksi

        Args:
            view: Uusi näkymä
        """

        self._current_view = view

    def _mover(self, view):
        """Sirrtää käyttöliittymän näkymän uuteen näkymään

        Args:
            view: Näkymä, johon siirrytään
        """
        
        self._close_current_view()
        self._set_view(view)
        self._current_view.pack()