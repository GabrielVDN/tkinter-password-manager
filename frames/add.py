import tkinter as tk
from tkinter import ttk


class Add(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)
        
        label_service = ttk.Label(self, text="Service*")
        label_service.grid(row=0, columnspan=2, padx=8, pady=8)
        
        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("Home"),
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=1, sticky="E", padx=8, pady=8)

        entry_service = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 16)
        )
        entry_service.grid(row=1, columnspan=2, padx=8, pady=(8, 18))

        label_username = ttk.Label(
            self, text="Username"
        )
        label_username.grid(row=2, columnspan=2, padx=8, pady=8)

        entry_username = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 16)
        )
        entry_username.grid(row=3, columnspan=2, padx=8, pady=(8, 18))

        label_password = ttk.Label(
            self, text="Password*"
        )
        label_password.grid(row=4, columnspan=2, padx=8, pady=8)

        entry_password = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 16)
        )
        entry_password.grid(row=5, columnspan=2, padx=8, pady=(8, 18))

        btn_add = ttk.Button(
            self,
            text="Add To Manager",
            cursor="hand2",
            width=18
        )
        btn_add.grid(row=6, columnspan=2, padx=8, pady=(8, 18))