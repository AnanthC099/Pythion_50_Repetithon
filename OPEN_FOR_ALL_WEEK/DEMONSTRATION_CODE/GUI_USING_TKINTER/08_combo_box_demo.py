from tkinter import * 
from tkinter import ttk 
import sys 

def onComboSelect(*args): 
    print("Current Selection:", day_variable.get())

def main(): 
    global day_variable
    root_window = Tk() 
    root_window.title("ComboBox Demo")

    frame = ttk.Frame(root_window, padding="3 3 12 12")
    frame.grid(column=1, row=1, sticky=(N,W,E,S))
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(1, weight=1)
 
    day_variable = StringVar()
    day_combo = ttk.Combobox(frame, textvariable=day_variable)
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    day_combo.configure(values=days)
    day_combo.grid(row=1, column=1, sticky=(W,))

    day_combo.bind("<<ComboboxSelected>>", onComboSelect)

    root_window.mainloop() 

main()