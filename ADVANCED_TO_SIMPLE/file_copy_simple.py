"""
Simplified version of SESSION-050/03-file-copy.py

ORIGINAL: Opens files without context managers (manual close() calls),
vulnerable to resource leaks if exception occurs.
SIMPLIFIED: Uses context managers (with statement) for safe file handling.
"""

source_file = "abc.txt"
destination_file = "lmn.txt"

with open(source_file, "r") as src, open(destination_file, "w") as dst:
    for line in src:
        dst.write(line)
