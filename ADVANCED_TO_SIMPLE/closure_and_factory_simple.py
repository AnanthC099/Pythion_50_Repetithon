"""
Simplified version of:
  - SESSION-085/01-Returning-Function-As-If-It-Were-A-Data-Object.py
  - SESSION-086/01-implicit-state-saving-revision.py
  - SESSION-086/02-FunctionFactory.py

ORIGINAL: Three separate files demonstrating closures, implicit state
saving, and function factories with verbose print/debug statements.
SIMPLIFIED: Combined into one file with clear examples and comments.
"""


# --- Example 1: Returning a function as data ---
def outer():
    def inner():
        print("inner() called")
    return inner


X = outer()
X()  # Calls the inner function via the returned reference


# --- Example 2: Implicit state saving (closure) ---
def make_greeter(name):
    def greet():
        print(f"Hello, {name}!")  # 'name' is captured from enclosing scope
    return greet


greet_alice = make_greeter("Alice")
greet_bob = make_greeter("Bob")
greet_alice()  # Hello, Alice!
greet_bob()    # Hello, Bob!


# --- Example 3: Function factory ---
def power_factory(n: int):
    def power(x: float):
        return x ** n  # 'n' is captured from enclosing scope
    return power


square = power_factory(2)
cube = power_factory(3)
raise_to_seven = power_factory(7)

print(f"square(2) = {square(2)}")              # 4
print(f"cube(2) = {cube(2)}")                  # 8
print(f"raise_to_seven(2) = {raise_to_seven(2)}")  # 128
