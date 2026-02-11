"""
Simplified version of 06_variables_type.py

ORIGINAL: Uses 4 global variables (int_val, float_val, str_val, bool_val).
SIMPLIFIED: Uses a class to hold all Tkinter variables.
"""

from tkinter import *
from tkinter import ttk
import sys


class VariableTypeDemo:
    def __init__(self):
        root = Tk()
        root.title("Different types of vars")

        frame = ttk.Frame(root, padding="3 3 12 12")
        frame.grid(row=0, column=0, sticky=(N, W, E, S))

        self.int_val = IntVar()
        self.float_val = DoubleVar()
        self.str_val = StringVar()
        self.bool_val = BooleanVar()

        fields = [
            ("Enter an integer number:", self.int_val),
            ("Enter a fractional number:", self.float_val),
            ("Enter a string:", self.str_val),
            ("Enter a boolean value:", self.bool_val),
        ]
        for i, (label, var) in enumerate(fields):
            ttk.Label(frame, text=label).grid(row=i + 1, column=1, sticky=(W, E))
            ttk.Entry(frame, textvariable=var).grid(row=i + 1, column=2, sticky=(W, E))

        ttk.Button(frame, text="Submit", command=self.on_submit).grid(row=5, column=1, sticky=(W, E))
        ttk.Button(frame, text="Exit", command=sys.exit).grid(row=6, column=1, sticky=(W, E))

        root.mainloop()

    def on_submit(self):
        for name, var in [("n", self.int_val), ("f", self.float_val),
                          ("s", self.str_val), ("b", self.bool_val)]:
            val = var.get()
            print(f"{name}:{val}. type({name}):{type(val)}")


if __name__ == "__main__":
    VariableTypeDemo()
