from tkinter import Tk
from ui.ui import UI, initRoot
import database

def main():
    exists = database.database_exists()
    connection = database.connect()
    if not exists:
        database.initialize(connection)

    root = Tk()
    initRoot(root)

    view = UI(root, connection)
    view.start()

    root.mainloop()


if __name__ == "__main__":
    main()
