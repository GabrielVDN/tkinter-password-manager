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
        work_label.grid(row=0, column=0, sticky="W")

        work_entry = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 14)
        )
        work_entry.grid(row=0, column=1)

        money_label = ttk.Label(
            self, text="Add money/hour:", style="Background.TLabel"
        )
        money_label.grid(row=1, column=0, sticky="W")

        money_entry = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 14)
        )
        money_entry.grid(row=1, column=1)

        tax_label = ttk.Label(
            self, text="Add tax in %:", style="Background.TLabel"
        )
        tax_label.grid(row=2, column=0, sticky="W")

        tax_entry = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 14)
        )
        tax_entry.grid(row=2, column=1)

        tax_label = ttk.Label(
            self, text="%", style="Background.TLabel"
        )
        tax_label.grid(row=2, column=2)

        extras_label = ttk.Label(
            self, text="Add your extra's:", style="Background.TLabel"
        )
        extras_label.grid(row=3, column=0, sticky="W")

        extras_entry = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 14)
        )
        extras_entry.grid(row=3, column=1)

        home_btn = ttk.Button(
            self,
            text="Home",
            command=show_home,
            cursor="hand2",
            style="Background.TButton"
        )
        home_btn.grid(row=4, column=0, sticky="EW")

        add_place_btn = ttk.Button(
            self,
            text="Add Place",
            command=lambda: [],
            cursor="hand2",
            style="Background.TButton"
        )
        add_place_btn.grid(row=4, column=1, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)