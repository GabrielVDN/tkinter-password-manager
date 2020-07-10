import tkinter as tk
from tkinter import ttk


class Home(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)


        # Set the widget's background.
        self["style"] = "Background.TFrame"

        workplaces = ["workplace 1", "workplace 2", "workplace 3"]
        select_workplace = ttk.Combobox(
            self,
            values=workplaces,
            state="readonly",
            style="Background.TCombobox"
        )
        select_workplace.grid()
        select_workplace.current(0)

        work_btn = ttk.Button(
            self,
            text="Settings",
            command=show_settings,
            cursor="hand2",
            style="Background.TButton"
        )
        work_btn.grid()

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)