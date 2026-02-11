"""
Simplified version of SESSION-068/02-try-except.py

ORIGINAL: Uses 'type(x) is not int and type(x) is not float' for validation.
SIMPLIFIED: Uses isinstance() with tuple of types.
"""


def my_square_root(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError(f"x must be int or float, got {type(x).__name__}")
    if x < 0:
        raise ValueError("x must be 0 or positive")
    return x ** 0.5


# --- Testing ---
print(f"sqrt(4.0) = {my_square_root(4.0)}")

try:
    my_square_root("Hello")
except TypeError as e:
    print(f"Caught: {e}")

print(f"sqrt(9.0) = {my_square_root(9.0)}")
print("----END OF PROGRAM----")
