from tkinter import * 
from tkinter import ttk 
import sys 

def onSubmit(): 
    n = int_val.get()
    print("n:{}. type(n):{}".format(n, type(n)))

    f = float_val.get() 
    print("f:{}. type(f):{}".format(f, type(f)))

    s = str_val.get() 
    print("s:{}. type(s):{}".format(s, type(s)))

    b = bool_val.get() 
    print("b:{}. type(b):{}".format(b, type(b)))

def main(): 
    global int_val, float_val, str_val, bool_val

    root_window = Tk()
    root_window.title("Different types of vars")

    frame = ttk.Frame(root_window, padding='3 3 12 12')
    frame.grid(row=0, column=0, sticky=(N,W,E,S))
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    msg_1 = ttk.Label(frame, text='Enter an integer number:')
    int_val = IntVar()
    E1 = ttk.Entry(frame, textvariable=int_val)

    msg_2 = ttk.Label(frame, text='Enter an fractional number:')
    float_val = DoubleVar()
    E2 = ttk.Entry(frame, textvariable=float_val)

    msg_3 = ttk.Label(frame, text='Enter a string:')
    str_val = StringVar()
    E3 = ttk.Entry(frame, textvariable=str_val)

    msg_4 = ttk.Label(frame, text='Enter a boolean value')
    bool_val = BooleanVar()
    E4 = ttk.Entry(frame, textvariable=bool_val)

    msg_1.grid(row=1, column=1, sticky=(W,E))
    E1.grid(row=1, column=2, sticky=(W,E))

    msg_2.grid(row=2, column=1, sticky=(W,E))
    E2.grid(row=2, column=2, sticky=(W,E))

    msg_3.grid(row=3, column=1, sticky=(W,E))
    E3.grid(row=3, column=2, sticky=(W,E))

    msg_4.grid(row=4, column=1, sticky=(W,E))
    E4.grid(row=4, column=2, sticky=(W,E))

    submit_button = ttk.Button(frame, text='Submit', command=onSubmit)
    submit_button.grid(row=5, column=1, sticky=(W,E))

    exit_button = ttk.Button(frame, text='Exit', command=sys.exit)
    exit_button.grid(row=6, column=1, sticky=(W,E))

    root_window.mainloop()

main()