from ui.views.mainView import MainView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = MainView(self._root)

    def start(self):
        self._current_view.pack()

    def _close_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _set_view(self, view):
      self._current_view = view
