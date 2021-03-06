import tkinter as tk
from tkinter import ttk
import json


class Home(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        label_1 = ttk.Label(
            self, textvariable=controller.login2, style="Background.TLabel"
        )
        label_1.grid(row=0, columnspan=3, padx=12, pady=(50,12))

        def onEnter(event):
            self.submit()

        self.entry_password = ttk.Entry(
            self, width=30,
            textvariable=controller.login3_password,
            font=("TkDefaultFont", 16), show='*'
        )
        self.entry_password.grid(row=1, columnspan=3, padx=12, pady=12)
        self.entry_password.bind("<Return>", onEnter)


        self.btn_submit = ttk.Button(
            self,
            text="Submit",
            cursor="hand2",
            command=lambda: self.submit(),
            style="Font.TButton"
        )
        self.btn_submit.grid(row=2, columnspan=3, padx=12, pady=12)
        
        # Create a new frame for the buttons.
        tframe = ttk.Frame(self, style="Background.TFrame")
        tframe.grid(row=3, columnspan=4, pady=(70,0))

        self.btn_add = ttk.Button(
            tframe,
            text=" 📝\nAdd",
            command=lambda: controller.show_frame("Add"),
            cursor="hand2",
            state='disabled',
            style="Font.TButton"
        )
        self.btn_add.grid(row=0, column=0)

        self.btn_list = ttk.Button(
            tframe,
            text="📃\nList",
            command=lambda: controller.show_frame("List"),
            cursor="hand2",
            state='disabled',
            style="Font.TButton"
        )
        self.btn_list.grid(row=0, column=1)

        self.btn_search = ttk.Button(
            tframe,
            text="  🔍\nSearch",
            command=lambda: controller.show_frame("Search"),
            cursor="hand2",
            state='disabled',
            style="Font.TButton"
        )
        self.btn_search.grid(row=0, column=2)

            
        for child in tframe.winfo_children():
            child.grid_configure(padx=12, pady=12)


    def submit(self):
        with open(self.controller.PATH_PASSWORD) as json_file:
            password = json.load(json_file)

        if self.controller.login3_password.get().strip() == password:
            self.controller.login2.set("logged in")
            self.entry_password.delete(0, 'end')
            
            self.entry_password['state'] = 'disabled'
            self.btn_submit['state'] = 'disabled'

            self.btn_add['state'] = 'normal'
            self.btn_list['state'] = 'normal'
            self.btn_search['state'] = 'normal'
            
        else:
            self.controller.login2.set(
                "Incorrect, try again."
            )
            self.entry_password.delete(0, 'end')
    
    def insert_data(self):
        pass
    
    def focus_entry(self):
        self.entry_password.focus()