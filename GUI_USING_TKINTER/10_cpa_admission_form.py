from tkinter import * 
from tkinter import ttk
import sys 

def show_info(course:str)->None: 
    win = Toplevel()
    L = ttk.Label(win, text=course+" Admin Info(DATE,DAYS,TIME,FEES)")
    L.grid(row=1, column=1, sticky=(W,))

def show_content(course:str)->None: 
    win = Toplevel()
    L = ttk.Label(win, text=course+" COURSE CONTENT")
    L.grid(row=1, column=1, sticky=(W,))

def configure_frame(fr:ttk.Frame, row=1, column=1, sticky=(N,W,E,S), weight=1) -> None:
    fr.grid(row=row, column=column, sticky=sticky)
    fr.rowconfigure(row, weight=weight)
    fr.columnconfigure(column, weight=weight)

def onClickContent():
    course_name = course_select_var.get()
    if course_name != "":
        show_content(course_name)

def onClickInfo():
    course_name = course_select_var.get()
    if course_name != "":
        show_info(course_name)

def onRepeaterCheckboxClick(): 
    global is_repeater 
    is_repeater = repeater_var.get() 

def onRegister() -> None: 
    global course_select_var, name_var, email_var, mobile_var
    global repeater_var, category_var

    course_name = course_select_var.get()
    if course_name == '': 
        print("No course is selected. Please select the course and then register")
        return None
    print("Course Name:", course_name)
    print("Name:", name_var.get())
    print("Email:", email_var.get())
    print("Mobile:", mobile_var.get())
    print("Student/Professional:", category_var.get())
    print("Is Repeater:", repeater_var.get())

def onClear():
    global course_select_var, name_var, email_var, mobile_var
    global repeater_var, category_var

    name_var.set('')
    email_var.set('')
    mobile_var.set(0)
    repeater_var.set('No')
    
def build_front_end(): 
    global course_select_var, name_var, email_var, mobile_var
    global repeater_var, category_var

    root_window = Tk() 
    root_window.title("CPA Admission Form")

    frames_relief = ['sunken', 'sunken', 'sunken', 'raised']
    frames = [] 
    for i in range(4): 
        frame = ttk.Frame(root_window, padding='3 3 12 12', relief=frames_relief[i])
        configure_frame(frame, row=i+1)
        frames.append(frame)
    title_frame, info_frame, input_frame, register_frame = frames
    
    title_of_form = ttk.Label(title_frame, text='CoreCode Programming Academy')
    title_of_form.grid(row=1, column=1, sticky=(W,E))

    course_select_var = StringVar()
    course_select_var.set('')

    r_texts = (
                "Masterclass in Assembly", 
                "Masterclass in C", 
                "Masterclass in C++", 
                "Masterclass in DSA", 
                "Masterclass in Python"
            )
  
    r_buttons = [] 
    for i in range(5): 
        r = ttk.Radiobutton(
                info_frame, 
                text=r_texts[i], 
                value=r_texts[i], 
                variable=course_select_var
            )
        r.grid(row=i+1, column=1, sticky=(W,))
        r_buttons.append(r)
    [r1,r2,r3,r4,r5] = r_buttons

    info_title = "Info"
    contents_title = 'Contents'
    contents_buttons = []
    info_buttons = []
    for i in range(5): 
        B = ttk.Button(info_frame, text=contents_title, command=onClickContent)
        B.grid(row=i+1, column=2, sticky=(E,))
        contents_buttons.append(B)
    for i in range(5): 
        B = ttk.Button(info_frame, text=info_title, command=onClickInfo)
        B.grid(row=i+1, column=3, sticky=(E,))
        info_buttons.append(B)
    
    msg1 = ttk.Label(input_frame, text="Name:")
    msg2 = ttk.Label(input_frame, text="Email:")
    msg3 = ttk.Label(input_frame, text="Mobile:")
    msg1.grid(row=1, column=1, sticky=('W', ))
    msg2.grid(row=2, column=1, sticky=('W', ))
    msg3.grid(row=3, column=1, sticky=('W', ))

    name_var, email_var = StringVar(), StringVar()
    mobile_var = IntVar()
    E1 = ttk.Entry(input_frame, width=30, textvariable=name_var)
    E2 = ttk.Entry(input_frame, textvariable=email_var)
    E3 = ttk.Entry(input_frame, textvariable=mobile_var)
    E1.grid(row=1, column=2, sticky=(W, E))
    E2.grid(row=2, column=2, sticky=(W, E))
    E3.grid(row=3, column=2, sticky=(W, E))

    category_var = StringVar()
    student_radio_button = ttk.Radiobutton(
                                input_frame, 
                                text="Student", 
                                value="Student",
                                variable=category_var
                            )
    professional_radio_button =  ttk.Radiobutton(
                                    input_frame, 
                                    text="Professional", 
                                    value="Professional", 
                                    variable=category_var
                                )
    student_radio_button.grid(row=4, column=1, sticky=(W,))
    professional_radio_button.grid(row=4, column=2, sticky=(W,))

    repeater_var = StringVar() 
    repeater_var.set("No")
    repeater_check_box = ttk.Checkbutton(
                                input_frame, 
                                text='Are you a repeater?', 
                                variable=repeater_var, 
                                onvalue='Yes', 
                                offvalue='No', 
                                command=onRepeaterCheckboxClick
                            )
    repeater_check_box.grid(row=5, column=1, sticky=(W,))

    register_button = ttk.Button(register_frame, text='Register', command=onRegister)
    register_button.grid(row=1, column=1, sticky=(W,E))

    clear_button = ttk.Button(register_frame, text='Clear', command=onClear)
    clear_button.grid(row=1, column=2, sticky=(W,E))

    exit_button = ttk.Button(register_frame, text='Exit', command=sys.exit)
    exit_button.grid(row=1, column=3, sticky=(W,E))

    root_window.mainloop()

def main(): 
    build_front_end()

main()

"""
Donald Knuth: The art of computer programming. 
Premature optimization is the root all evils. 
"""

"""
1) Object Oriented Analysis and Design with application -> Grady Booch 
    (min first 5 chapters)
2) The UML Guide -> Booch, Jacobson, Rambaugh 
3) Software Engineering : A practitioner's approach -> Rodger Pressman
4) Clean Coding

5) Design Patterns -> Gamma, Ulrich, Vissides, Helm -> Gang of four
"""