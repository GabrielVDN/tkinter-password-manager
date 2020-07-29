import tkinter as tk
from tkinter import ttk


class Search(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        entry_search = ttk.Entry(
            self,
            width=48,
            font=("TkDefaultFont", 16)
        )
        entry_search.grid(row=0, column=0)
        
        label_search = ttk.Button(
            self,
            text="🔍",
            width=3
        )
        label_search.grid(row=0, column=1)
        
        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("Home"),
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=2, sticky="E")


        # Create a new frame for the treeview.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=3)

        columns = ['id', 'Service', 'Username*', 'Password']

        tree = ttk.Treeview(
            tframe, columns=columns, height=18, show="headings"
        )
        tree.column("id", width=30)

        for col in columns[1:]:
            tree.column(col, width=350)
            tree.heading(col, text=col)

        tree.pack(side="left", fill="y")

        scrollbar = ttk.Scrollbar(tframe, orient='vertical')
        scrollbar.configure(command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.config(yscrollcommand=scrollbar.set)

        
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=8)