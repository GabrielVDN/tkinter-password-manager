import tkinter as tk
from tkinter import ttk

class Search(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Give the Widget a name.
        # self.title("Search For Credentials")


        entry_search = ttk.Entry(
            self,
            width=18,
            font=("TkDefaultFont", 16)
        )
        entry_search.grid(row=0, column=0)
        
        label_search = ttk.Label(self, text="Search")
        label_search.grid(row=0, column=1)


        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)