import tkinter as tk
from tkinter import ttk


class List(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        tframe1=tk.Frame(self)
        tframe1.pack(side='top')
        headings = ["Service", "Username"]

        # Adding the Treeview
        tk.Label(tframe1, text="Double Click to copy password",
                bd=2).pack(side='left', padx=10,pady=10)
        btn_back = ttk.Button(
            tframe1,
            text="🔙",
            command=lambda: controller.show_frame("Home"),
            cursor="hand2",
            width=3
        )
        btn_back.pack(side='left', padx=10,pady=10)


        tframe2=tk.Frame(self)
        tframe2.pack(side='bottom')

        scroll = ttk.Scrollbar(tframe2, orient='vertical', takefocus=True)
        self.tree = ttk.Treeview(tframe2, columns=headings, show="headings")
        scroll.config(command=self.tree.yview)
        self.tree.configure(yscroll=scroll.set)

        scroll.pack(side='right', fill='y')
        self.tree.pack(side='left', fill='both', expand=1)

        # Adding headings to the columns and resp. cmd's
        for heading in headings:
            self.tree.heading(
                heading, text=heading,
                command=lambda c=heading: self.sortby(self.tree, c, 0))
            self.tree.column(heading, width=400)