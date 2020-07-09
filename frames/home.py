import tkinter as tk
from tkinter import ttk


class Home(ttk.Frame):
    def __init__(self, parent, controller, show_work):
        super().__init__(parent)

        label = ttk.Label(self, text="Home")

        work_btn = ttk.Button(
            self,
            text="Work",
            command=show_work,
            cursor="hand2"
        )
        work_btn.grid()

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)