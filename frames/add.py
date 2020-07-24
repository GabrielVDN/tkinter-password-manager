import tkinter as tk
from tkinter import ttk


class Add(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller    


        # # Give the Widget a name.
        # self.title("Add Credentials")
        
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        
        label_service = ttk.Label(self, text="Service*")
        label_service.grid(row=0, column=0)

        entry_service = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 16)
        )
        entry_service.grid(row=1, column=0)

        label_username = ttk.Label(
            self, text="Username"
        )
        label_username.grid(row=2, column=0)

        entry_username = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 16)
        )
        entry_username.grid(row=3, column=0)

        label_password = ttk.Label(
            self, text="Password*"
        )
        label_password.grid(row=4, column=0)

        entry_password = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 16)
        )
        entry_password.grid(row=5, column=0)
        

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)