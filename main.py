import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import Home, Work
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


class WorkManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Background.TFrame", background="#7fd49c")

        self.columnconfigure(0, weight=1)


        # Set the widget's background.
        self["background"] = "#7fd49c"
        # Give the Widget a name.
        self.title("My Work Manager")
        # Give the Widget a size.
        self.geometry("600x400")

        # Set the overall fontsize to 15 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=24)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = {}

        work_frame = Work(container, self, lambda: self.show_frame(Home))
        home_frame = Home(container, self, lambda: self.show_frame(Work))
        work_frame.grid(row=0, column=0, sticky="NESW")
        home_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Work] = work_frame
        self.frames[Home] = home_frame
        
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


app = WorkManager()
app.mainloop()