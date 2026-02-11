"""
Simplified version of SESSION-023/04-make-square-gui.py

ORIGINAL: Uses module-level globals (output_msg_label, output_msg_control,
input_box_control, root_window), scattered widget creation at module level.
SIMPLIFIED: Uses a class to hold state, clean organization.
"""

from tkinter import *


class MakeSquareGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Make Square GUI Version")
        self.root.geometry("300x200")

        Label(self.root, text="Enter a number to square:").grid(row=0, column=0)

        self.input_var = StringVar()
        Entry(self.root, textvariable=self.input_var).grid(row=0, column=1)

        self.output_var = StringVar()
        Label(self.root, textvariable=self.output_var).grid(row=1, column=0)

        Button(self.root, text="Compute", command=self.compute).grid(row=2, column=0)
        Button(self.root, text="Clear", command=self.clear).grid(row=2, column=1)
        Button(self.root, text="Exit", command=self.root.destroy).grid(row=2, column=2)

        self.root.mainloop()

    def compute(self):
        n = int(self.input_var.get())
        self.output_var.set(f"Square of {n} is: {n * n}")

    def clear(self):
        self.input_var.set("")
        self.output_var.set("")


if __name__ == "__main__":
    MakeSquareGUI()
