import tkinter as tk
from tkinter import ttk


class Work(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)


        # Set the widget's background.
        self["style"] = "Background.TFrame"

        label = ttk.Label(
            self, text="Work", style="Background.TLabel"
        )
        label.grid()

        work_btn = ttk.Button(
            self,
            text="Home",
            command=show_home,
            cursor="hand2",
            style="Background.TButton"
        )
        work_btn.grid()

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)