from tkinter import * 
from tkinter import ttk 

def onSubmit(): 
    subject_name = selected_course_var.get()
    print("Selected Course is {}:".format(subject_name))

def main(): 
    global selected_course_var
    
    root_window = Tk() 
    root_window.title("RadioButton Demo")

    frame = ttk.Frame(root_window, padding='3 3 12 12')
    frame.grid(row=0, column=0, sticky=(N,W,E,S))
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    selected_course_var = StringVar()

    cpa_101 = ttk.Radiobutton(  
                                frame, 
                                variable=selected_course_var, 
                                text="Masterclass in Assembly",
                                value="Masterclass in Assembly"
                            )
    cpa_102 = ttk.Radiobutton(  
                                frame, 
                                variable=selected_course_var, 
                                text="MasterClass in C",
                                value="MasterClass in C"
                            )
    cpa_103 = ttk.Radiobutton(  
                                frame, 
                                variable=selected_course_var, 
                                text="Masterclass in C++",
                                value="Masterclass in C++"
                            )
    cpa_101.grid(row=1, column=1, sticky=(W,E))
    cpa_102.grid(row=2, column=1, sticky=(W,E))
    cpa_103.grid(row=3, column=1, sticky=(W,E))

    submit_button = ttk.Button(frame)
    submit_button.configure(text='Submit', command=onSubmit)
    submit_button.grid(row=4, column=1, sticky=(W,E))

    root_window.mainloop()

main()