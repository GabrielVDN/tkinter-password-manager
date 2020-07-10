import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)


        # Set the widget's background.
        self["style"] = "Background.TFrame"

        label = ttk.Label(
            self, text="Settings", style="Background.TLabel"
        )
        label.grid()

        settings_btn = ttk.Button(
            self,
            text="Home",
            command=show_home,
            cursor="hand2",
            style="Background.TButton"
        )
        settings_btn.grid()

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)