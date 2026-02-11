"""
Simplified version of 05_compute_gravitational_gui.py

ORIGINAL: Uses 4 global variables, bare except with sys.exc_info(),
verbose .configure() calls on separate lines.
SIMPLIFIED: Uses a class, specific exception handling, inline widget config.
"""

from tkinter import *
from tkinter import ttk, messagebox
import sys


class GravitationalCalculator:
    DEFAULT_MSG = "The output will be displayed here"

    def __init__(self):
        root = Tk()
        root.title("Gravitational Force Calculator")

        self.m1_var = StringVar()
        self.m2_var = StringVar()
        self.r_var = StringVar()
        self.output_var = StringVar(value=self.DEFAULT_MSG)

        # Input frame
        input_frame = ttk.Frame(root, padding="3 3 12 12", borderwidth=10, relief="raised")
        input_frame.grid(column=1, row=1, sticky=(N, W, E, S))

        fields = [
            ("Enter mass of body 1 in kgs:", self.m1_var),
            ("Enter mass of body 2 in kgs:", self.m2_var),
            ("Enter the distance between the bodies in meters:", self.r_var),
        ]
        for i, (label, var) in enumerate(fields):
            ttk.Label(input_frame, text=label).grid(column=1, row=i + 1, sticky=(W, E))
            ttk.Entry(input_frame, textvariable=var).grid(column=2, row=i + 1, sticky=(W, E))

        # Button frame
        btn_frame = ttk.Frame(root, padding="3 3 12 12", borderwidth=10, relief="raised")
        btn_frame.grid(column=1, row=2, sticky=(N, W, E, S))

        ttk.Button(btn_frame, text="Compute", command=self.compute).grid(column=1, row=1, sticky=(W, E))
        ttk.Button(btn_frame, text="Clear", command=self.clear).grid(column=2, row=1, sticky=(W, E))
        ttk.Button(btn_frame, text="Exit", command=sys.exit).grid(column=3, row=1, sticky=(W, E))

        # Output frame
        output_frame = ttk.Frame(root, padding="3 3 12 12", borderwidth=10, relief="sunken")
        output_frame.grid(column=1, row=3, sticky=(N, W, E, S))
        ttk.Label(output_frame, textvariable=self.output_var).grid(column=1, row=1, sticky=(W, E))

        for frame in root.winfo_children():
            frame.grid_configure(padx=3, pady=1)
            for widget in frame.winfo_children():
                widget.grid_configure(padx=5, pady=5)

        root.mainloop()

    def compute(self):
        try:
            m1 = float(self.m1_var.get())
            m2 = float(self.m2_var.get())
            r = float(self.r_var.get())
            if m1 <= 0 or m2 <= 0 or r <= 0:
                raise ValueError("Mass and distance must be positive")
            G = 6.67e-11
            F = (G * m1 * m2) / (r ** 2)
            self.output_var.set(f"Gravitational force: {F} Newton")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear(self):
        self.m1_var.set("")
        self.m2_var.set("")
        self.r_var.set("")
        self.output_var.set(self.DEFAULT_MSG)


if __name__ == "__main__":
    GravitationalCalculator()
