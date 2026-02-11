# Package import section 
from tkinter import *

# Variable definition section 
output_msg_label = None 
output_msg_control = None
input_box_control = None 
root_window = None

# Event handler section
def compute_button_handler():
    n = int(input_box_control.get())
    result = n * n
    result_str = str(result)
    output_str = 'Square of ' + str(n) + ' is: ' + result_str
    output_msg_control.set(output_str) 

def clear_button_handler():
    input_box_control.set('')
    output_msg_control.set('')

def exit_button_handler():
    root_window.destroy()

# Main window and widgets creation section
root_window = Tk()
root_window.title('Make Square GUI Version')
root_window.geometry('300x200') 

input_msg_label = Label(root_window)
input_msg_label.configure(text='Enter a number to square:')
input_msg_label.grid(row=0, column=0) 

input_box_control = StringVar() 
input_box = Entry(root_window)
input_box.configure(textvariable=input_box_control)
input_box.grid(row=0, column=1)

output_msg_control = StringVar()
output_msg_label = Label(root_window)
output_msg_label.configure(textvariable=output_msg_control)
output_msg_label.grid(row=1, column=0)
output_msg_control.set('')

compute_button = Button(root_window)
compute_button.configure(text='Compute', command=compute_button_handler)
compute_button.grid(row=2, column=0)

clear_button = Button(root_window)
clear_button.configure(text='Clear', command=clear_button_handler)
clear_button.grid(row=2, column=1) 

exit_button = Button(root_window)
exit_button.configure(text='Exit', command=exit_button_handler)
exit_button.grid(row=2, column=2)

# Entering event loop section 
root_window.mainloop() 
