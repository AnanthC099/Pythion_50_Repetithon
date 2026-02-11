from tkinter import * 
from tkinter import ttk 
import sys 

def onFileNew(): 
    print("Menubar->File->New")

def onFileOpen(): 
    print("Menubar->File->Open")

def onFileSave(): 
    print("Menubar->File->Save")

def onFileSaveAs(): 
    print("Menubar->File->Save As")

def onFileExit(): 
    print("Menubar->File->Exit")
    sys.exit(0)

def onEditUndo(): 
    print("Menubar->Edit->Undo")

def onEditRedo(): 
    print("Menunbar->Edit->Redo")

def onEditCut(): 
    print("Menubar->Edit->Cut")

def onEditCopy(): 
    print("Menubar->Edit->Copy")

def onEditPaste():
    print("Menubar->Edit->Paste")

def main(): 
    root_window = Tk()
    root_window.title("HelloWin")
    root_window.option_add('*tearOff', False)
    
    menu_bar = Menu(root_window)
    root_window.configure(menu=menu_bar)
    file_menu = Menu(menu_bar)
    edit_menu = Menu(menu_bar)

    menu_bar.add_cascade(menu=file_menu, label='File')
    menu_bar.add_cascade(menu=edit_menu, label='Edit')

    file_menu.add_command(label='New', command=onFileNew)
    file_menu.add_command(label='Open', command=onFileOpen)
    file_menu.add_separator()
    file_menu.add_command(label='Save', command=onFileSave)
    file_menu.add_command(label='SaveAs', command=onFileSaveAs)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=onFileExit)
    
    root_window.mainloop()

main() 

"""
What can you add by simply looking into a documentation: 
1) Keyboard Shortcut: 
File
New     ctrl + N 
Save    ctrl + s 

Edit
Cut     ctrl + c 
Paste   ctrl + v 

2) Associated CheckButton (or RadioButton)

3) Suboptions to a command
"""