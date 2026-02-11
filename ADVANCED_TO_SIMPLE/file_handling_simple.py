"""
Simplified version of SESSION-045/01-file-handling.py

ORIGINAL: Opens files without context managers, manual close() calls,
two separate open/close cycles for write then read.
SIMPLIFIED: Uses context managers (with statement) for safe file handling.
"""

# Step 1: Create and write to a file using context manager
with open("abc.txt", "w") as f:
    print("This is a first line in the file", file=f)
    print("CoreCode Programming Academy", file=f)
    for x in [True, 10, 3.14, "Hello"]:
        print(x, file=f)
    print("This is the last line in the file", file=f)

# Step 2: Read and display the file using context manager
with open("abc.txt", "r") as f:
    for line in f:
        print(line, end="")
