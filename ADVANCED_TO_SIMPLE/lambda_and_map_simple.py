"""
Simplified version of:
  - SESSION-073/power_lambda_map.py
  - SESSION-073/LAMBDA-IDLE-LOG.py
  - SESSION-072/02-relation-between-def-and-lambda.py

ORIGINAL: Scattered across multiple files and IDLE logs, some with
typos (b&y instead of b*y), verbose inline comments.
SIMPLIFIED: Combined lambda/map concepts into one clean file.
"""


# --- Lambda is shorthand for a simple function ---
# lambda:
square = lambda n: n ** 2
# equivalent def:
def square_def(n):
    return n ** 2

print(f"lambda: {square(5)}, def: {square_def(5)}")  # Both: 25


# --- Lambda with default arguments ---
weighted_sum = lambda x, y, z=1.5: x + y * z
print(f"weighted_sum(10, 20) = {weighted_sum(10, 20)}")      # 40.0
print(f"weighted_sum(10, 20, 2) = {weighted_sum(10, 20, 2)}")  # 50


# --- Lambda with *args (variadic) ---
show_all = lambda *args: print(args)
show_all(100, 200, 300)  # (100, 200, 300)


# --- map() applies a function to every item ---
with open("test.txt", "r") as f:
    for line in map(lambda line: line.upper(), f):
        print(line, end="")
