"""
Simplified version of 08_combo_box_demo.py

ORIGINAL: Uses global variable (day_variable),
also passes command= to Combobox (not supported).
SIMPLIFIED: Uses a class, correct event binding.
"""

from tkinter import *
from tkinter import ttk


class ComboBoxDemo:
    def __init__(self):
        root = Tk()
        root.title("ComboBox Demo")

        frame = ttk.Frame(root, padding="3 3 12 12")
        frame.grid(column=1, row=1, sticky=(N, W, E, S))

        self.day_var = StringVar()
        days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

        combo = ttk.Combobox(frame, textvariable=self.day_var, values=days)
        combo.grid(row=1, column=1, sticky=(W,))
        combo.bind("<<ComboboxSelected>>", self.on_select)

        root.mainloop()

    def on_select(self, *args):
        print("Current Selection:", self.day_var.get())


if __name__ == "__main__":
    ComboBoxDemo()
