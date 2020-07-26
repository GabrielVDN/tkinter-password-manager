import tkinter as tk
from tkinter import ttk


class List(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        label_1 = ttk.Label(
            self, text="Double Click To Copy Password"
        )
        label_1.grid(row=0, column=0)
        
        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("Home"),
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=1, sticky="E")


        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=8)