"""
Simplified version of 03_textvariable_demo.py

ORIGINAL: Uses global variables (msg, i) shared between functions.
SIMPLIFIED: Uses a class to hold state, no globals needed.
"""

from tkinter import *
from tkinter import ttk


class TextVariableDemo:
    MESSAGES = ["HELLO-1", "HELLO-10", "HELLO-100"]

    def __init__(self):
        self.i = -1
        root = Tk()
        root.title("Text Variable Demo")

        self.msg = StringVar(value="START")
        ttk.Label(root, textvariable=self.msg).grid(row=1, column=1)
        Button(root, text="Change", command=self.on_change).grid(row=1, column=0)

        root.mainloop()

    def on_change(self):
        self.i = (self.i + 1) % len(self.MESSAGES)
        self.msg.set(self.MESSAGES[self.i])
        print(self.msg.get())


if __name__ == "__main__":
    TextVariableDemo()
