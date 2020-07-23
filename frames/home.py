import tkinter as tk
from tkinter import ttk
import calendar
import datetime



class Home(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)


        # Set the widget's background.
        self["style"] = "Background.TFrame"

        workplaces = ["workplace 1", "workplace 2", "workplace 3"]
        select_workplace = ttk.Combobox(
            self,
            values=workplaces,
            state="readonly",
            font=("TkDefaultFont", 16),
            style="Background.TCombobox"
        )
        select_workplace.grid(row=0, column=0)
        select_workplace.current(0)

        settings_btn = ttk.Button(
            self,
            text="Settings",
            command=show_settings,
            cursor="hand2",
            width=9,
            style="Background.TButton"
        )
        settings_btn.grid(row=0, column=1)

        period_label = ttk.Label(
            self,
            text="Period:",
            style="Background.TLabel"
        )
        period_label.grid(row=1, column=0, sticky="W")

        def showCal() : 
            # Create a GUI window 
            new_gui = tk.Tk() 
            # Set the background colour of GUI window 
            new_gui.config(background = "white") 
            # set the name of tkinter GUI window  
            new_gui.title("CALENDER")

            
            
            for child in new_gui.winfo_children():
                child.grid_configure(padx=12, pady=12)
                
            # start the GUI  
            new_gui.mainloop()

        cal_btn = ttk.Button(
            self,
            text="Calendar",
            command=showCal,
            cursor="hand2",
            width=9,
            style="Background.TButton"
        )
        cal_btn.grid(row=1, column=1)

        get_btn = ttk.Button(
            self,
            text="Get",
            cursor="hand2",
            style="Background.TButton"
        )
        get_btn.grid(row=2, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)