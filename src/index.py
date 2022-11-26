from tkinter import Tk
from ui.ui import UI, initRoot

def main():

    root = Tk()
    initRoot(root)

    view = UI(root)
    view.start()

    root.mainloop()


if __name__ == "__main__":
    main()
