"""
Simplified version of 04_feet_to_meter.py

ORIGINAL: Uses global variables (feet, meters) shared between functions,
bare except clause silently swallows errors.
SIMPLIFIED: Uses a class, specific exception handling.
"""

from tkinter import *
from tkinter import ttk


class FeetToMeterConverter:
    def __init__(self):
        root = Tk()
        root.title("Feet to meter conversion")

        frame = ttk.Frame(root, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.feet = StringVar()
        self.meters = StringVar()

        ttk.Entry(frame, width=7, textvariable=self.feet).grid(column=2, row=1, sticky=(W, E))
        ttk.Label(frame, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(frame, text="Convert", command=self.calculate).grid(column=3, row=3, sticky=W)
        ttk.Label(frame, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(frame, text="Is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(frame, text="meters").grid(column=3, row=2, sticky=W)

        for widget in frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        root.bind("<Return>", self.calculate)
        root.mainloop()

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            if value < 0:
                raise ValueError("Cannot enter negative value")
            meter_value = round(0.3048 * value, 4)
            self.meters.set(meter_value)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    FeetToMeterConverter()
