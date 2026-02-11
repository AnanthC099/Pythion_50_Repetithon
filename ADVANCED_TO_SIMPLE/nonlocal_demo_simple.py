"""
Simplified version of SESSION-084/07-nonlocal-demo.py

ORIGINAL: Two examples with deeply nested functions (f1/f2/f3/f4),
verbose print statements.
SIMPLIFIED: Same concepts, cleaner naming, clear before/after output.
"""


# --- Example 1: nonlocal modifies enclosing variable ---
def outer():
    n = 500

    def inner():
        nonlocal n
        n = 1000

    print(f"Before inner(): n = {n}")  # 500
    inner()
    print(f"After inner(): n = {n}")   # 1000


outer()
print("---")


# --- Example 2: nonlocal reaches through multiple nesting levels ---
def level1():
    n = 100

    def level2():
        def level3():
            nonlocal n
            n = 200
        level3()

    print(f"Before: n = {n}")   # 100
    level2()
    print(f"After: n = {n}")    # 200


level1()
