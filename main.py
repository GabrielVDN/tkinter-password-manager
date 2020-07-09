import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import Home, Work
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


class WorkManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use("clam")

        self.title("My Work Manager")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

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