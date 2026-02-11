"""
Simplified version of SESSION-069/01-last-raised-exception-info.py

ORIGINAL: Uses bare except with sys.exc_info() and manual
traceback.print_tb() for exception inspection.
SIMPLIFIED: Uses 'except Exception as e' with traceback module,
cleaner and more Pythonic.
"""

import traceback


def f3(x):
    if x < 0:
        raise ValueError("x cannot be less than 0")
    print(x)


def f2(y):
    f3(y)


def f1(z):
    f2(z)


def main():
    try:
        f1(-100)
    except ValueError as e:
        print(f"Exception: {type(e).__name__}: {e}")
        print("----- Traceback -----")
        traceback.print_exc()
        print("----- End -----")

    print("Program continues after handling the exception.")


main()
