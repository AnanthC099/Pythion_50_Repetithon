"""
Simplified version of 10_cpa_admission_form.py

ORIGINAL (Advanced): 6+ global variable declarations, repetitive widget
creation code, scattered function definitions all relying on globals.

SIMPLIFIED: Uses a single class to hold all state (no globals),
loops to reduce repetitive widget creation, cleaner structure.
"""

from tkinter import *
from tkinter import ttk
import sys


class AdmissionForm:
    COURSES = (
        "Masterclass in Assembly",
        "Masterclass in C",
        "Masterclass in C++",
        "Masterclass in DSA",
        "Masterclass in Python",
    )

    def __init__(self):
        self.root = Tk()
        self.root.title("CPA Admission Form")

        # Variables
        self.course_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.mobile_var = IntVar()
        self.category_var = StringVar()
        self.repeater_var = StringVar(value="No")

        self.build_ui()
        self.root.mainloop()

    def build_ui(self):
        # Title frame
        title_frame = ttk.Frame(self.root, padding="3 3 12 12", relief="sunken")
        title_frame.grid(row=1, column=1, sticky=(N, W, E, S))
        ttk.Label(title_frame, text="CoreCode Programming Academy").grid(row=1, column=1, sticky=(W, E))

        # Course selection frame
        course_frame = ttk.Frame(self.root, padding="3 3 12 12", relief="sunken")
        course_frame.grid(row=2, column=1, sticky=(N, W, E, S))

        for i, course in enumerate(self.COURSES):
            ttk.Radiobutton(course_frame, text=course, value=course,
                            variable=self.course_var).grid(row=i + 1, column=1, sticky=(W,))
            ttk.Button(course_frame, text="Contents",
                       command=self.show_content).grid(row=i + 1, column=2, sticky=(E,))
            ttk.Button(course_frame, text="Info",
                       command=self.show_info).grid(row=i + 1, column=3, sticky=(E,))

        # Input frame
        input_frame = ttk.Frame(self.root, padding="3 3 12 12", relief="sunken")
        input_frame.grid(row=3, column=1, sticky=(N, W, E, S))

        fields = [("Name:", self.name_var), ("Email:", self.email_var), ("Mobile:", self.mobile_var)]
        for i, (label, var) in enumerate(fields):
            ttk.Label(input_frame, text=label).grid(row=i + 1, column=1, sticky=(W,))
            ttk.Entry(input_frame, textvariable=var).grid(row=i + 1, column=2, sticky=(W, E))

        ttk.Radiobutton(input_frame, text="Student", value="Student",
                        variable=self.category_var).grid(row=4, column=1, sticky=(W,))
        ttk.Radiobutton(input_frame, text="Professional", value="Professional",
                        variable=self.category_var).grid(row=4, column=2, sticky=(W,))

        ttk.Checkbutton(input_frame, text="Are you a repeater?",
                        variable=self.repeater_var, onvalue="Yes",
                        offvalue="No").grid(row=5, column=1, sticky=(W,))

        # Button frame
        btn_frame = ttk.Frame(self.root, padding="3 3 12 12", relief="raised")
        btn_frame.grid(row=4, column=1, sticky=(N, W, E, S))

        ttk.Button(btn_frame, text="Register", command=self.on_register).grid(row=1, column=1, sticky=(W, E))
        ttk.Button(btn_frame, text="Clear", command=self.on_clear).grid(row=1, column=2, sticky=(W, E))
        ttk.Button(btn_frame, text="Exit", command=sys.exit).grid(row=1, column=3, sticky=(W, E))

    def show_content(self):
        course = self.course_var.get()
        if course:
            win = Toplevel()
            ttk.Label(win, text=f"{course} COURSE CONTENT").grid(row=1, column=1, sticky=(W,))

    def show_info(self):
        course = self.course_var.get()
        if course:
            win = Toplevel()
            ttk.Label(win, text=f"{course} Admin Info (DATE, DAYS, TIME, FEES)").grid(row=1, column=1, sticky=(W,))

    def on_register(self):
        course = self.course_var.get()
        if not course:
            print("No course selected. Please select a course first.")
            return
        print(f"Course: {course}")
        print(f"Name: {self.name_var.get()}")
        print(f"Email: {self.email_var.get()}")
        print(f"Mobile: {self.mobile_var.get()}")
        print(f"Category: {self.category_var.get()}")
        print(f"Repeater: {self.repeater_var.get()}")

    def on_clear(self):
        self.name_var.set("")
        self.email_var.set("")
        self.mobile_var.set(0)
        self.repeater_var.set("No")


if __name__ == "__main__":
    AdmissionForm()
