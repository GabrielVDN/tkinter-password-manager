import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox


class Add(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        label_service = ttk.Label(self, text="Service*", style="Background.TLabel")
        label_service.grid(row=0, columnspan=2, padx=8, pady=8)
        
        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: [controller.show_frame("Home"), self.empty_entry()],
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=1, sticky="E", padx=8, pady=8)

        def onEnter1(event):
            self.entry_username.focus()

        self.entry_service = ttk.Entry(
            self,
            width=18,
            textvariable=controller.add_service,
            font=("TkDefaultFont", 16)
        )
        self.entry_service.grid(row=1, columnspan=2, padx=8, pady=(8, 18))
        self.entry_service.bind("<Return>", onEnter1)

        label_username = ttk.Label(
            self, text="Username", style="Background.TLabel"
        )
        label_username.grid(row=2, columnspan=2, padx=8, pady=8)

        def onEnter2(event):
            self.entry_password.focus()

        self.entry_username = ttk.Entry(
            self,
            width=18,
            textvariable=controller.add_username,
            font=("TkDefaultFont", 16)
        )
        self.entry_username.grid(row=3, columnspan=2, padx=8, pady=(8, 18))
        self.entry_username.bind("<Return>", onEnter2)

        label_password = ttk.Label(
            self, text="Password*", style="Background.TLabel"
        )
        label_password.grid(row=4, columnspan=2, padx=8, pady=8)

        def onEnter3(event):
            self.add_data()
            self.entry_service.focus()

        self.entry_password = ttk.Entry(
            self,
            width=18,
            textvariable=controller.add_password,
            font=("TkDefaultFont", 16)
        )
        self.entry_password.grid(row=5, columnspan=2, padx=8, pady=(8, 18))
        self.entry_password.bind("<Return>", onEnter3)

        btn_add = ttk.Button(
            self,
            text="Add To Manager",
            cursor="hand2",
            width=18,
            command=lambda: self.add_data(),
            style="Font.TButton"
        )
        btn_add.grid(row=6, columnspan=2, padx=8, pady=(8, 18))

        self.last_nmr = tk.IntVar() # Default; value=0

        with open(self.controller.path_data.get()) as json_file:
            data_list = json.load(json_file)

        try:
            last_dict = data_list[-1]
            self.last_nmr.set(list(last_dict.keys())[0])
        except:
            pass


    def add_data(self):
        if self.controller.add_service.get().strip() != '' and self.controller.add_password.get().strip() != '':
            self.last_nmr.set(self.last_nmr.get() + 1)

            with open(self.controller.path_data.get()) as json_file:
                data_list = json.load(json_file)

            data = {}
            data[self.last_nmr.get()] = {
                'Service': self.controller.add_service.get().strip(),
                'Username': self.controller.add_username.get().strip(),
                'Password': self.controller.add_password.get().strip()
            }
            data_list.append(data)

            with open(self.controller.path_data.get(), 'w') as outfile:
                json.dump(data_list, outfile, indent=2)

            self.empty_entry()
        else:
            messagebox.showerror("No Input", "You need to input something in Service and Password!")
            self.entry_service.focus()

    def empty_entry(self):
        self.entry_password.delete(0,'end')
        self.entry_service.delete(0,'end')
        self.entry_username.delete(0,'end')
    
    def insert_data(self):
        pass
    
    def focus_entry(self):
        self.entry_service.focus()