from tkinter import Tk
from ui.ui import UI

def main():
    root = Tk()
    root.geometry("300x250")
    root.resizable(False,False)
    root.title("Timer")

    view = UI(root)
    view.start()

    root.mainloop()

if __name__ == "__main__":
    main()