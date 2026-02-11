"""
Simplified version of SESSION-076/List-Comprehension-General-Format-And-Some-Examples.py

ORIGINAL: Uses undefined 'iterable' and 'path' variables (pseudocode mixed
with runnable code), no clear separation.
SIMPLIFIED: All examples are runnable with concrete values.
"""

# --- Four general forms of list comprehension ---

# Form 1: [expr for x in iterable]
squares = [x ** 2 for x in range(5)]
print("Squares:", squares)  # [0, 1, 4, 9, 16]

# Form 2: [expr for x in iterable if condition]
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)  # [0, 4, 16, 36, 64]

# Form 3: [f(x) for x in iterable]
chars = [c * 5 for c in "Hello"]
print("Repeated:", chars)  # ['HHHHH', 'eeeee', ...]

# Form 4: [f(x) for x in iterable if condition]
alpha_repeated = [c * 3 for c in "Hello World!" if c.isalpha()]
print("Alpha x3:", alpha_repeated)
