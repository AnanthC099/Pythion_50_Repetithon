from tkinter import * 
from tkinter import ttk             

def onAddToPath(): 
    current_selection = add_to_path_var.get()
    print(current_selection)

def main(): 
    global add_to_path_var
    
    root_window = Tk()
    root_window.title("Checkbox Demo")

    frame = ttk.Frame(root_window, padding = "3 3 12 12")
    frame.grid(row=0, column=0, sticky=(N,W,E,S))
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    add_to_path_var = StringVar() 
    add_to_path_check_box = ttk.Checkbutton(
                                frame, 
                                text='Add to Path', 
                                variable=add_to_path_var, 
                                onvalue='relative', 
                                offvalue='absolute', 
                                command=onAddToPath
                            )
    add_to_path_check_box.grid(row=1, column=1, sticky=(W,E))

    root_window.mainloop() 

main()