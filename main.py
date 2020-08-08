import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import json
import os
from frames.login import Login
from frames.home import Home
from frames.add import Add
from frames.list import List
from frames.search import Search
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


path_appdata = os.getenv("APPDATA")
# Check if the datafolder exist.
# If not, create it.
if not os.path.exists(path_appdata+'\\password-manager'):
    os.mkdir(path_appdata+'\\password-manager')

    data = []
    with open(path_appdata+'\\password-manager\\data.json', 'w') as outfile:
        json.dump(data, outfile)

    password = ""
    with open(path_appdata+'\\password-manager\\password.json', 'w') as outfile:
        json.dump(password, outfile)


# Create a Tkinter Widget.
class PasswordManager(tk.Tk): 
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self)
        container.grid()

        # Set the style to 'clam'.
        style = ttk.Style()
        style.theme_use("clam")

        # Create some custom styles.
        style.configure("Background.TFrame", background="#F0F0F0")
        
        style.configure("Background.TLabel", background="#F0F0F0")

        style.configure(
            "Font.TButton",
            font=("TkDefaultFont", 15),
            relief="solid"
        )
        style.map(
            "Font.TButton",
            font=[("active",  ("TkDefaultFont", 17))]
        )

        style.configure('Data.Treeview', rowheight=45)

        # Give the Widget a name.
        self.title("Password Manager")
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 16 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=16)

        # Create all needed tk.-variables.
        self.path_data = tk.StringVar(value=path_appdata+'\\password-manager\\data.json')
        self.path_password = tk.StringVar(value=path_appdata+'\\password-manager\\password.json')

        self.login1 = tk.StringVar(
            value="Choose a log-in password\nfor this Password Manager."
        )
        self.login2 = tk.StringVar(value="Log In")

        self.login1_password = tk.StringVar()
        self.login2_password = tk.StringVar()
        self.login3_password = tk.StringVar()

        self.add_service = tk.StringVar()
        self.add_username = tk.StringVar()
        self.add_password = tk.StringVar()

        self.search_name = tk.StringVar()


        self.frames = {}
        for F in (Login,Home, Add, List, Search):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        
        with open(self.path_password.get()) as json_file:
            password = json.load(json_file)

        if password == "":
            self.show_frame("Login")
        else:
            self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.insert_data()
        frame.focus_entry()


GUI = PasswordManager()
GUI.mainloop()