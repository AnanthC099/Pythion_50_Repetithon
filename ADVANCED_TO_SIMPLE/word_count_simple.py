"""
Simplified version of SESSION-052/word_count.py and wc1.py

ORIGINAL: Uses 'type(s) is not str', state machine with IN/OUT
constants, 'currentState is OUT' identity comparison on integers.
SIMPLIFIED: Uses isinstance(), Python's built-in split() for
word counting (much simpler), or a cleaner state machine.
"""

import sys


def get_word_count(s: str) -> int:
    """Count words in a string using split()."""
    if not isinstance(s, str):
        return -1
    return len(s.split())


def count_file(file_path: str) -> None:
    """Count lines, words, and characters in a file."""
    line_count = word_count = char_count = 0

    with open(file_path, "r") as f:
        for line in f:
            line_count += 1
            word_count += get_word_count(line)
            char_count += len(line)

    print(f"File: {file_path}")
    print(f"  Lines: {line_count}")
    print(f"  Words: {word_count}")
    print(f"  Characters: {char_count}")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} file_path")
        sys.exit(1)
    count_file(sys.argv[1])


if __name__ == "__main__":
    main()
