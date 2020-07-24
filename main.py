import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames.home import Home
from frames.add import Add
from frames.list import List
from frames.search import Search
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


# Create a Tkinter Widget.
class PasswordManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self)
        container.grid()

        # Set the style to 'clam'.
        style = ttk.Style()
        style.theme_use("clam")

        # Set the widget's background.
        self["background"] = "white"
        # Give the Widget a name.
        self.title("Password Manager")
        # Give the Widget a size.
        self.geometry("900x460")
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 15 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=20)

        # Create all needed tk.-variables.
        self.login = tk.StringVar(value="Log In")

        self.frames = {}
        for F in (Home, Add, List, Search):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


GUI = PasswordManager()
GUI.mainloop()