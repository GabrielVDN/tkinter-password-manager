import tkinter as tk
from tkinter import ttk


class Login(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        label_1 = ttk.Label(
            self, textvariable=controller.login1
        )
        label_1.grid(row=0, column=0, pady=(100,12))

        self.entry_password = ttk.Entry(
            self, width=30,
            font=("TkDefaultFont", 16)
        )
        self.entry_password.grid(row=1, column=0, pady=12)


        self.btn_submit = ttk.Button(
            self,
            text="Submit",
            cursor="hand2",
            command=lambda: self.submit()
        )
        self.btn_submit.grid(row=2, column=0, pady=12)

        self.x = tk.IntVar(value=1)

    
    def submit(self):
        if self.x.get() == 2:
            self.controller.show_frame("Home")

        self.controller.login1.set("Repeat it!")
        self.entry_password.delete(0, 'end')
        self.x.set(2)