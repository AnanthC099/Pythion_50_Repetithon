from tkinter import * 


root_window = None 


def ok_button_handler():
    print('Ok Button is clicked')


def cancel_button_handler():
    print('Cancel button is clicked')


def retry_button_handler():
    print('Retry button is clicked')


def exit_button_handler():
    root_window.destroy()


root_window = Tk()
root_window.title('Four Button Demo')
root_window.geometry('300x200') 

ok_button = Button(root_window)
ok_button.configure(text='Ok', command=ok_button_handler)
ok_button.grid(row=0, column=0)

cancel_button = Button(root_window)
cancel_button.configure(text='Cancel', command=cancel_button_handler)
cancel_button.grid(row=1, column=0)

retry_button = Button(root_window)
retry_button.configure(text='Retry', command=retry_button_handler)
retry_button.grid(row=2, column=0)

exit_button = Button(root_window)
exit_button.configure(text='Exit', command=exit_button_handler)
exit_button.grid(row=3, column=0)

root_window.mainloop() 
