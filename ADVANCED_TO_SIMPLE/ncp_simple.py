"""
Simplified version of SESSION-052/ncp.py

ORIGINAL: Uses 'type(x) is not str' for validation,
manual file handle open/close, while loop with index.
SIMPLIFIED: Uses isinstance(), context managers, for loop.
"""

import sys


def copy_file(source: str, destination: str) -> bool:
    if not isinstance(source, str) or not isinstance(destination, str):
        return False

    with open(source, "r") as src, open(destination, "a") as dst:
        for line in src:
            dst.write(line)
    return True


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} src1 src2 ... srcN destination")
        sys.exit(1)

    destination = sys.argv[-1]
    for source in sys.argv[1:-1]:
        if not copy_file(source, destination):
            print(f"Error copying {source}")
            sys.exit(1)

    print("All files copied successfully")


if __name__ == "__main__":
    main()
