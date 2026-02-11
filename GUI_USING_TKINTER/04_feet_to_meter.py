from tkinter import * 
from tkinter import ttk 


feet = None 
meters = None


def calculate(*args: tuple) -> None: 
    global feet, meters 
    try: 
        value = float(feet.get())
        if value < 0: 
            raise ValueError("Cannot enter negative value")
        meter_value = int(0.3048 * value * 10000.0 + 0.5)/10000.0
        meters.set(meter_value)
    except: 
        pass 


def main(): 
    global feet, meters 

    root_window = Tk()
    root_window.title("Feet to meter conversion")
    
    master_frame = ttk.Frame(root_window, padding="3 3 12 12") 
    master_frame.grid(column=0, row=0, sticky=(N,W,E,S))

    root_window.columnconfigure(0, weight = 1)
    root_window.rowconfigure(0, weight = 1)
    
    feet = StringVar() 
    feet_entry = ttk.Entry(master_frame, width = 7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W,E))

    meters = StringVar() 
    label_handle = ttk.Label(master_frame, textvariable=meters)
    label_handle.grid(column=2, row=2, sticky=(W,E))

    button_handle = ttk.Button(master_frame)
    button_handle.configure(text = "Convert", command = calculate) 
    button_handle.grid(column=3, row=3, sticky=W)

    feet_label = ttk.Label(master_frame)
    feet_label.configure(text = "feet")
    feet_label.grid(column=3, row=1, sticky=W)

    msg_label = ttk.Label(master_frame) 
    msg_label.configure(text="Is equivalent to")
    msg_label.grid(column=1, row=2, sticky=E)

    meter_label = ttk.Label(master_frame)
    meter_label.configure(text="meters") 
    meter_label.grid(column=3, row=2, sticky=W)

    for widget in master_frame.winfo_children(): 
        widget.grid_configure(padx=5, pady=5)

    feet_entry.focus() 
    root_window.bind("<Return>", calculate)
    root_window.mainloop()


main() 
