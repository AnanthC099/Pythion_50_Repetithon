"""
Simplified version of 09_radio_button.py

ORIGINAL: Uses global variable (selected_course_var),
repetitive Radiobutton creation code.
SIMPLIFIED: Uses a class, loop for radio button creation.
"""

from tkinter import *
from tkinter import ttk


class RadioButtonDemo:
    COURSES = ("Masterclass in Assembly", "Masterclass in C", "Masterclass in C++")

    def __init__(self):
        root = Tk()
        root.title("RadioButton Demo")

        frame = ttk.Frame(root, padding="3 3 12 12")
        frame.grid(row=0, column=0, sticky=(N, W, E, S))

        self.selected_course = StringVar()

        for i, course in enumerate(self.COURSES):
            ttk.Radiobutton(
                frame, text=course, value=course,
                variable=self.selected_course,
            ).grid(row=i + 1, column=1, sticky=(W, E))

        ttk.Button(frame, text="Submit", command=self.on_submit).grid(
            row=len(self.COURSES) + 1, column=1, sticky=(W, E)
        )

        root.mainloop()

    def on_submit(self):
        print(f"Selected Course: {self.selected_course.get()}")


if __name__ == "__main__":
    RadioButtonDemo()
