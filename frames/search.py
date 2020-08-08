import tkinter as tk
from tkinter import ttk
import json
import pyperclip


class Search(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        def onEnter(event):
            empty_tree(None)
            self.search()
            self.entry_search.delete(0,'end')
            self.focus_entry()

        self.entry_search = ttk.Entry(
            self,
            width=48,
            textvariable=controller.search_name,
            font=("TkDefaultFont", 16)
        )
        self.entry_search.grid(row=0, column=0)
        self.entry_search.bind("<Return>", onEnter)

        label_search = ttk.Button(
            self,
            text="🔍",
            width=3,
            command=lambda: [
                empty_tree(None),
                self.search(),
                self.entry_search.delete(0,'end'),
                self.focus_entry()
            ]
        )
        label_search.grid(row=0, column=1)
        
        def empty_tree(event):
            for i in self.tree.get_children():
                self.tree.delete(i)

        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: [controller.show_frame("Home"), self.entry_search.delete(0,'end'), empty_tree(None)],
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=2, sticky="E")


        # Create a new frame for the treeview.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=3)

        columns = ['id', 'Service', 'Username*', 'Password']

        self.tree = ttk.Treeview(
            tframe, columns=columns, show="headings", style='Data.Treeview'
        )
        self.tree.column("id", width=45)
        self.tree.column("Service", width=300)
        self.tree.column("Username*", width=600)
        self.tree.column("Password", width=300)
        self.tree.pack(side="left", fill="y")
        self.tree.bind("<Double-1>", self.OnDoubleClick)

        for col in columns:
            self.tree.heading(col, text=col)

        scrollbar = ttk.Scrollbar(tframe, orient='vertical')
        scrollbar.configure(command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")

        self.tree.config(yscrollcommand=scrollbar.set)

        
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=8)


    def search(self, *args):
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
            for t in tuples_values:
                if self.controller.search_name.get().strip().lower() in t.lower() and self.controller.search_name.get().strip() != "":
                    try:
                        self.tree.insert("", "end", values=tuples_values)
                        # Delte the tuple because else it could show twice.
                        del tuples_values
                    except:
                        pass
  
    def OnDoubleClick(self, event):
        item = self.tree.focus()

        # Copies password to clipboard
        copy_password = self.tree.item(item, "values")[3]
        pyperclip.copy(copy_password)


    def insert_data(self):
        pass
    
    def focus_entry(self):
        self.entry_search.focus()