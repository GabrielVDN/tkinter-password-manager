import tkinter as tk
from tkinter import ttk


class Home(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # # Give the Widget a name.
        # self.title("Password Manager")


        label_1 = ttk.Label(
            self, textvariable=controller.login
        )
        label_1.grid(row=0, columnspan=3)

        entry_password = ttk.Entry(
            self, width=30,
            font=("TkDefaultFont", 18), show='*'
        )
        entry_password.grid(row=1, columnspan=3)

        btn_submit = ttk.Button(
            self,
            text="Submit",
            cursor="hand2",
        )
        btn_submit.grid(row=2, columnspan=3)

        btn_add = ttk.Button(
            self,
            text="Add",
            command=lambda: controller.show_frame("Add"),
            cursor="hand2",
        )
        btn_add.grid(row=3, column=0)

        btn_list = ttk.Button(
            self,
            text="List",
            command=lambda: controller.show_frame("List"),
            cursor="hand2",
        )
        btn_list.grid(row=3, column=1)

        btn_search = ttk.Button(
            self,
            text="Search",
            command=lambda: controller.show_frame("Search"),
            cursor="hand2",
        )
        btn_search.grid(row=3, column=2)

            
        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)