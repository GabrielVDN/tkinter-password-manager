import tkinter as tk
from tkinter import ttk


class Home(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        label_1 = ttk.Label(
            self, textvariable=controller.login
        )
        label_1.grid(row=0, columnspan=3, padx=12, pady=(50,12))

        entry_password = ttk.Entry(
            self, width=30,
            font=("TkDefaultFont", 16), show='*'
        )
        entry_password.grid(row=1, columnspan=3, padx=12, pady=12)

        btn_submit = ttk.Button(
            self,
            text="Submit",
            cursor="hand2",
        )
        btn_submit.grid(row=2, columnspan=3, padx=12, pady=12)

        
        # Create a new frame for the buttons.
        tframe = ttk.Frame(self)
        tframe.grid(row=3, columnspan=4, pady=(70,0))

        btn_add = ttk.Button(
            tframe,
            text=" 📝\nAdd",
            command=lambda: controller.show_frame("Add"),
            cursor="hand2",
        )
        btn_add.grid(row=0, column=0)

        btn_list = ttk.Button(
            tframe,
            text="📃\nList",
            command=lambda: controller.show_frame("List"),
            cursor="hand2",
        )
        btn_list.grid(row=0, column=1)

        btn_search = ttk.Button(
            tframe,
            text="  🔍\nSearch",
            command=lambda: controller.show_frame("Search"),
            cursor="hand2",
        )
        btn_search.grid(row=0, column=2)

            
        for child in tframe.winfo_children():
            child.grid_configure(padx=12, pady=12)