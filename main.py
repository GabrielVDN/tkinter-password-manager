import tkinter as tk
from tkinter import ttk
from ctypes import windll
 
# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
    
    
class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("640x200")
        self.title("Title Here")

        label = ttk.Label(self, text="Tkinet window")
        label.config(font=("Comic Sans MS",40))
        label.pack()

root = HelloWorld()
 
root.mainloop()