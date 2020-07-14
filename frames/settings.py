import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)


        # Set the widget's background.
        self["style"] = "Background.TFrame"

        label_workplace = ttk.Label(
            self, text="Add work place:", style="Background.TLabel"
        )
        label_workplace.grid(row=0, column=0, sticky="W")

        self.entry_workplace = ttk.Entry(
            self,
            width=18,
            textvariable=controller.workplace,
            font=("TkDefaultFont", 14)
        )
        self.entry_workplace.grid(row=0, column=1)

        label_maney = ttk.Label(
            self, text="Add money/hour:", style="Background.TLabel"
        )
        label_maney.grid(row=1, column=0, sticky="W")

        self.entry_money = ttk.Entry(
            self,
            width=18,
            textvariable=controller.money,
            font=("TkDefaultFont", 14)
        )
        self.entry_money.grid(row=1, column=1)

        label_tax = ttk.Label(
            self, text="Add tax in %:", style="Background.TLabel"
        )
        label_tax.grid(row=2, column=0, sticky="W")

        self.entry_tax = ttk.Entry(
            self,
            width=18,
            textvariable=controller.tax,
            font=("TkDefaultFont", 14)
        )
        self.entry_tax.grid(row=2, column=1)

        label_percent = ttk.Label(
            self, text="%", style="Background.TLabel"
        )
        label_percent.grid(row=2, column=2)

        label_extras = ttk.Label(
            self, text="Add your extra's:", style="Background.TLabel"
        )
        label_extras.grid(row=3, column=0, sticky="W")

        self.entry_extra = ttk.Entry(
            self,
            width=18,
            textvariable=controller.extra,
            font=("TkDefaultFont", 14)
        )
        self.entry_extra.grid(row=3, column=1)

        btn_home = ttk.Button(
            self,
            text="Home",
            command=show_home,
            cursor="hand2",
            style="Background.TButton"
        )
        btn_home.grid(row=4, column=0, sticky="EW")

        btn_add_place = ttk.Button(
            self,
            text="Add Place",
            command=lambda: [
                print(f"Added place:\n{controller.workplace.get()},\n{controller.money.get()},\n{controller.tax.get()}, {controller.extra.get()}"),
                self.empty_entrys()
            ],
            cursor="hand2",
            style="Background.TButton"
        )
        btn_add_place.grid(row=4, column=1, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)

    def empty_entrys(self):
        self.entry_workplace.delete(0,"end")
        self.entry_money.delete(0,"end")
        self.entry_tax.delete(0,"end")
        self.entry_extra.delete(0,"end")