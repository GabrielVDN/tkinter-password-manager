import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)


        # Set the widget's background.
        self["style"] = "Background.TFrame"

        work_label = ttk.Label(
            self, text="Add work place:", style="Background.TLabel"
        )
        work_label.grid(row=0, column=0)

        work_entry = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 14)
        )
        work_entry.grid(row=0, column=1)

        money_label = ttk.Label(
            self, text="Add money/hour:", style="Background.TLabel"
        )
        money_label.grid(row=1, column=0)

        money_entry = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 14)
        )
        money_entry.grid(row=1, column=1)

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