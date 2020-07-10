import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import Home, Settings
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


class WorkManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Background.TFrame", background="#7fd49c")
        style.configure("Background.TLabel", background="#7fd49c")
        style.configure(
            "Background.TButton",
            background="#4a855e",
            bordercolor="black",
            relief="solid"
        )  
        style.map(
            "Background.TButton",
            background=[("active", "#3e704f")],
            font=[("active",  ("TkDefaultFont", 25)), ("pressed",  ("TkDefaultFont", 26))]
        )


        # Set the widget's background.
        self["background"] = "#7fd49c"
        # Give the Widget a name.
        self.title("My Work Manager")
        # Give the Widget a size.
        self.geometry("800x400")
        # Put everything in the middle.
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 15 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=24)


        container = ttk.Frame(self)
        container.grid()

        self.frames = {}

        settings_frame = Settings(container, self, lambda: self.show_frame(Home))
        home_frame = Home(container, self, lambda: self.show_frame(Settings))
        settings_frame.grid(row=0, column=0, sticky="NESW")
        home_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Settings] = settings_frame
        self.frames[Home] = home_frame
        
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


app = WorkManager()
app.mainloop()