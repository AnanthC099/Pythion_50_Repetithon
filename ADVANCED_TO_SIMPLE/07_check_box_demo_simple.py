"""
Simplified version of 07_check_box_demo.py

ORIGINAL: Uses global variable (add_to_path_var).
SIMPLIFIED: Uses a class to hold state.
"""

from tkinter import *
from tkinter import ttk


class CheckboxDemo:
    def __init__(self):
        root = Tk()
        root.title("Checkbox Demo")

        frame = ttk.Frame(root, padding="3 3 12 12")
        frame.grid(row=0, column=0, sticky=(N, W, E, S))

        self.add_to_path_var = StringVar()
        ttk.Checkbutton(
            frame, text="Add to Path",
            variable=self.add_to_path_var,
            onvalue="relative", offvalue="absolute",
            command=self.on_toggle,
        ).grid(row=1, column=1, sticky=(W, E))

        root.mainloop()

    def on_toggle(self):
        print(self.add_to_path_var.get())


if __name__ == "__main__":
    CheckboxDemo()
