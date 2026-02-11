from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
import sys 

default_msg = "The output will be displayed here"

def do_compute():
    try: 
        m1 = float(m1_str_var.get())
        m2 = float(m2_str_var.get())
        r = float(r_str_var.get())
        if m1 <= 0.0 or m2 <= 0.0 or r <= 0.0: 
            raise ValueError("Mass and distance must be positive real numbers")
        G = 6.67 * (10 ** -11)
        F = (G * m1 * m2) / (r**2)
        output_msg = "The amount of gravitational force between the bodies is ({}) Newton".format(F)
        output_str_var.set(output_msg)
    except: 
        exc_name, exc_data, exc_tb = sys.exc_info()
        error_msg = "Error Type:{}. Error Message:{}.Try again".format(exc_name.__name__, str(exc_data))
        messagebox.askquestion("Error", error_msg)

def do_clear(): 
    empty_str = ''
    m1_str_var.set(empty_str)
    m2_str_var.set(empty_str)
    r_str_var.set(empty_str)
    output_str_var.set(default_msg)

def create_front_end():
    global m1_str_var, m2_str_var, r_str_var, output_str_var, default_msg

    root_window = Tk() 
    root_window.title("Gravitational Force Calculator")
 
    input_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    input_frame.grid(column=1, row=1, sticky=(N,W,E,S))
    input_frame.rowconfigure(1, weight=1)
    input_frame.columnconfigure(1, weight=1)

    m1_msg = ttk.Label(input_frame)
    m1_msg.configure(text='Enter mass of body 1 in kgs:')
    m1_msg.grid(column=1, row=1, sticky=(W,E))

    m2_msg = ttk.Label(input_frame)
    m2_msg.configure(text='Enter mass of body 2 in kgs:')
    m2_msg.grid(column=1, row=2, sticky=(W,E))

    r_msg = ttk.Label(input_frame)
    r_msg.configure(text='Enter the distance between the bodies in meters:')
    r_msg.grid(column=1, row=3, sticky=(W,E))

    m1_str_var = StringVar()
    m1_entry = ttk.Entry(input_frame)
    m1_entry.configure(textvariable=m1_str_var)
    m1_entry.grid(column=2, row=1, sticky=(W,E))

    m2_str_var = StringVar() 
    m2_entry = ttk.Entry(input_frame)
    m2_entry.configure(textvariable=m2_str_var)
    m2_entry.grid(column=2, row=2, sticky=(W,E))

    r_str_var = StringVar() 
    r_entry = ttk.Entry(input_frame)
    r_entry.configure(textvariable=r_str_var)
    r_entry.grid(column=2, row=3, sticky=(W,E))

    button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    button_frame.grid(column=1, row=2, sticky=(N,W,E,S))
    button_frame.rowconfigure(2, weight=1)
    button_frame.columnconfigure(1, weight=1)

    compute_button = ttk.Button(button_frame)
    compute_button.configure(text="Compute", command=do_compute)
    compute_button.grid(column=1, row=1, sticky=(W,E))

    clear_button = ttk.Button(button_frame)
    clear_button.configure(text="Clear", command=do_clear)
    clear_button.grid(column=2, row=1, sticky=(W,E))

    exit_button = ttk.Button(button_frame)
    exit_button.configure(text='Exit', command=sys.exit)
    exit_button.grid(column=3, row=1, sticky=(W,E))

    output_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='sunken')
    output_frame.grid(column=1, row=3, sticky=(N,W,E,S))
    output_frame.rowconfigure(3, weight=1)
    output_frame.columnconfigure(1, weight=1)

    output_str_var = StringVar()
    output_msg = ttk.Label(output_frame)
    output_msg.configure(textvariable=output_str_var)
    output_msg.grid(column=1, row=1, sticky=(W,E))
    output_str_var.set(default_msg)

    for frames in root_window.winfo_children(): 
        frames.grid_configure(padx=3, pady=1)
        for widget in frames.winfo_children(): 
            widget.grid_configure(padx=5, pady=5)

    root_window.mainloop()

def main(): 
    create_front_end()
    
main() 

"""
serverside of the line 
input_frame = ttk.Frame(root_window, padding='3 3 12 12', borderwidth=10, relief='raised')

class Frame:
    Frame_attr = ['padding', 'borderwidth', 'relief', etc.] 
    def __init__(self, window_handle, **kwargs): 
        self.window_handle = window_handle 
        for (attr, val) in kwargs.items(): 
            if attr in Frame.Frame_attr:
"""