import tkinter 
import tkinter.ttk
import sys 

def terminate(): 
    print("exiting the app...")
    sys.exit(0)

root_window = tkinter.Tk() 
root_window.title("Test Window")

master_frame = tkinter.ttk.Frame(root_window, padding = "3 3 12 12")
master_frame.grid(row=0, column=0, sticky=(tkinter.N, tkinter.W,tkinter.E,tkinter.S))

B = tkinter.Button(master_frame)
B.configure(text="EXIT BUTTON", command=terminate)
B.grid(row=1, column=1, sticky=tkinter.E)

root_window.mainloop()




