import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox


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
            textvariable=controller.login1_password,
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
            if self.controller.login1_password.get().strip() == self.controller.login2_password.get():
                with open('password.txt', 'w') as outfile:
                    json.dump(self.controller.login2_password.get(), outfile, indent=2)

                self.controller.show_frame("Home")
            else:
                self.controller.login1.set(
                    "Incorrect, try again! Or to reset:\nclose the app and open it again."
                )

        else:
            if len(self.controller.login1_password.get().strip()) >= 6:
                self.controller.login2_password.set(self.controller.login1_password.get().strip())
                self.controller.login1.set("Repeat it!")
                self.entry_password.delete(0, 'end')
                self.x.set(2)

            else:
                messagebox.showerror(
                    "Invalid Input", "Your Password needs to be 6 or more characters!"
                )