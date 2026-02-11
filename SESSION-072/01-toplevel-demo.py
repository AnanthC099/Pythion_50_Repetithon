from tkinter import * 

n = 0 

def onButtonClick():
    global n 
    n = n + 1  
    win = Toplevel()
    L = Label(win, text=f'{n}th window is launched')
    L.grid(row=1, column=1)
    
def main(): 
    root_window = Tk() 
    root_window.title("Toplevel Window Demo")

    B = Button(root_window, text='Launch New Window')
    B.configure(command=onButtonClick)
    B.grid(row=1, column=1)

    root_window.mainloop() 

main()