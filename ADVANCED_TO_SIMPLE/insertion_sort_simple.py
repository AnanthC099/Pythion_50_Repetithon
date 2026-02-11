"""
Simplified version of SESSION-017/insertion_sort.py

ORIGINAL: Uses type(L) != list for type checking.
SIMPLIFIED: Uses isinstance() for proper type checking.
"""


def insertion_sort(L: list[int]) -> None:
    if not isinstance(L, list):
        raise TypeError("Expected a list")
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i > -1 and L[i] > key:
            L[i + 1] = L[i]
            i -= 1
        L[i + 1] = key


L = [50, 40, 30, 20, 10]
print("Before:", L)
insertion_sort(L)
print("After:", L)
