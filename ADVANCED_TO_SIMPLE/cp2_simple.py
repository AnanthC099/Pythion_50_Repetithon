"""
Simplified version of SESSION-051/cp2.py

ORIGINAL: Uses 'type(x) is not str' for validation,
manual file handle open/close without context managers.
SIMPLIFIED: Uses isinstance(), context managers (with statement).
"""

import sys


def copy_file(source: str, destination: str) -> bool:
    if not isinstance(source, str) or not isinstance(destination, str):
        return False

    with open(source, "r") as src, open(destination, "w") as dst:
        for line in src:
            dst.write(line)
    return True


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} source_file destination_file")
        sys.exit(1)

    if copy_file(sys.argv[1], sys.argv[2]):
        print("File copied successfully")
    else:
        print("Error copying file")
        sys.exit(1)


if __name__ == "__main__":
    main()
