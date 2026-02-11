"""
Simplified version of SESSION-021/02-toggle-message.py

ORIGINAL: Uses globals (msg_num, control_msg, root_window),
module-level widget creation code mixed with function definitions.
SIMPLIFIED: Uses a class, clean structure.
"""

from tkinter import *


class ToggleDemo:
    MESSAGES = [
        "I am learning Python Programming Language",
        "I am learning GUI Programming using tkinter",
    ]

    def __init__(self):
        self.msg_index = 0

        self.root = Tk()
        self.root.title("Toggle Demo")
        self.root.geometry("300x200")

        self.msg_var = StringVar(value=self.MESSAGES[0])
        Label(self.root, textvariable=self.msg_var).grid(row=0, column=0)
        Button(self.root, text="Toggle", command=self.toggle).grid(row=1, column=0)

        self.root.mainloop()

    def toggle(self):
        self.msg_index = 1 - self.msg_index
        self.msg_var.set(self.MESSAGES[self.msg_index])


if __name__ == "__main__":
    ToggleDemo()
