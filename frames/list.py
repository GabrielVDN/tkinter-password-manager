import tkinter as tk
from tkinter import ttk


class List(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Adding the Treeview
        label_1 = ttk.Label(self, text="Double Click to copy password")
        label_1.grid(row=0, columnspan=2)

        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("Home"),
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=1, sticky="E")

        
        # Create a new frame for the treeview.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=2)

        tree = ttk.Treeview(
            tframe, height=18, columns=["Service", "Username*", "Password"], show="headings"
        )
        tree.pack(side='left')

        vsb = ttk.Scrollbar(tframe, orient="vertical", command=tree.yview)
        vsb.pack(side='right', fill='y')

        tree.configure(yscrollcommand=vsb.set)

        tree.heading("1", text="Account")
        tree.insert('', 'end', values=['1a', '1b', '1c'])
        tree.insert('', 'end', values=['2a', '2b', '2c'])
        tree.insert('', 'end', values=['3a', '3b', '3c'])
        tree.insert('', 'end', values=['4a', '4b', '4c'])
        tree.insert('', 'end', values=['5a', '5b', '5c'])
        tree.insert('', 'end', values=['6a', '6b', '6c'])
        tree.insert('', 'end', values=['7a', '7b', '7c'])
        tree.insert('', 'end', values=['8a', '8b', '8c'])
        tree.insert('', 'end', values=['9a', '9b', '9c'])
        tree.insert('', 'end', values=['10a', '10b', '10c'])
        tree.insert('', 'end', values=['11a', '11b', '11c'])
        tree.insert('', 'end', values=['12a', '12b', '12c'])
        tree.insert('', 'end', values=['13a', '13b', '13c'])


        # Adding headings to the columns and resp. cmd's
        for heading in ["Service", "Username*", "Password"]:
            tree.heading(
                heading, text=heading)
            tree.column(heading, width=375)


        for child in self.winfo_children():
            child.grid_configure(padx=(12,0), pady=8)