"""
Simplified version of SESSION-072/01-toplevel-demo.py

ORIGINAL: Uses global variable n modified inside event handler.
SIMPLIFIED: Uses a class to hold state.
"""

from tkinter import *


class ToplevelDemo:
    def __init__(self):
        self.count = 0
        root = Tk()
        root.title("Toplevel Window Demo")

        Button(root, text="Launch New Window", command=self.on_click).grid(row=1, column=1)

        root.mainloop()

    def on_click(self):
        self.count += 1
        win = Toplevel()
        Label(win, text=f"{self.count}th window is launched").grid(row=1, column=1)


if __name__ == "__main__":
    ToplevelDemo()
