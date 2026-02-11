"""
Simplified version of SESSION-052/wc2.py

ORIGINAL: Uses 'type(s) is not str', state machine with integer identity
comparison ('is OUT'), while loop with index, no context manager.
SIMPLIFIED: Uses isinstance(), str.split() for word count, for loop,
context manager.
"""

import sys


def get_word_count(s: str) -> int:
    if not isinstance(s, str):
        return -1
    return len(s.split())


def count_file(file_path: str) -> tuple[int, int, int]:
    line_count = word_count = char_count = 0
    with open(file_path, "r") as f:
        for line in f:
            line_count += 1
            word_count += get_word_count(line)
            char_count += len(line)
    return line_count, word_count, char_count


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_path(s)")
        sys.exit(1)

    total_lines = total_words = total_chars = 0

    for file_path in sys.argv[1:]:
        lines, words, chars = count_file(file_path)
        print(f"{lines}\t{words}\t{chars}\t{file_path}")
        total_lines += lines
        total_words += words
        total_chars += chars

    if len(sys.argv) > 2:
        print(f"{total_lines}\t{total_words}\t{total_chars}\ttotal")


if __name__ == "__main__":
    main()
