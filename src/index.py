from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Enter username or click create user.")

        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)

        login_button = ttk.Button(master=self._root, text="Login")
        signup_button = ttk.Button(master=self._root, text="Create user")

        heading_label.grid(row=0, column=0, columnspan=4)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        login_button.grid(row=3, column=0, columnspan=2)
        signup_button.grid(row=3, column=2, columnspan=2)


window = Tk()
window.title("Login")

ui = UI(window)
ui.start()

window.mainloop()