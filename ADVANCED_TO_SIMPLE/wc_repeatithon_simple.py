"""
Simplified version of SESSION-053/01-word-count-repeatithon.py and 02-wc1.py

ORIGINAL: Contains 5+ duplicate definitions of the same function with bugs
(missing colons, 'is' for integer comparison, 'currentstate' typo).
Massive code repetition for processing the same file.
SIMPLIFIED: Single correct function, reusable file processing in a loop.
"""


def get_word_count(s: str) -> int:
    if not isinstance(s, str):
        return -1
    return len(s.split())


def count_file(file_name: str) -> None:
    line_count = word_count = char_count = 0
    with open(file_name, "r") as f:
        for line in f:
            line_count += 1
            word_count += get_word_count(line)
            char_count += len(line)
    print(f"{line_count}\t{word_count}\t{char_count}\t{file_name}")


# Process multiple files without repeating code
for file_name in ["abc.txt", "pqr.txt"]:
    count_file(file_name)
