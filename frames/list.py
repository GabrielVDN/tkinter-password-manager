import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox
import pyperclip


class List(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Adding the Treeview
        label_1 = ttk.Label(self, text="Double Click to copy password", style="Background.TLabel")
        label_1.grid(row=0, columnspan=2)

        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: [controller.show_frame("Home"), empty_tree(None)],
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=1, sticky="E")

        def empty_tree(event):
            for i in self.tree.get_children():
                self.tree.delete(i)

        
        # Create a new frame for the treeview.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=2)

        columns = ('id', 'Service', 'Username*', 'Password')

        self.tree = ttk.Treeview(
            tframe, columns=columns, show="headings", style='Data.Treeview'
        )
        self.tree.column("id", width=45)
        self.tree.column("Service", width=300)
        self.tree.column("Username*", width=600)
        self.tree.column("Password", width=300)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.tree.pack(side="left", fill="y")

        for col in columns:
            self.tree.heading(col, text=col)

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

  
    def OnDoubleClick(self, event):
        item = self.tree.focus()

        # Copies password to clipboard
        copy_password = self.tree.item(item, "values")[3]
        pyperclip.copy(copy_password)

    def insert_data(self):
        """
        Insertion method.
        """
        try:
            with open(self.controller.path_data.get()) as json_file:
                data_list = json.load(json_file)

            list_values = []
            
            for i in data_list:
                tuples_values = []

                for x in i.keys():
                    tuples_values.append(x)
                for y in i.values():
                    for z in y.values():
                        tuples_values.append(z)

                list_values.append(tuple(tuples_values))

            amount = 0
            while amount < len(list_values):
                self.tree.insert("", "end", values=list_values[amount])
                amount+=1

        except:
            messagebox.showerror(
                "No Data", "There is no data.")
    
    def focus_entry(self):
        pass