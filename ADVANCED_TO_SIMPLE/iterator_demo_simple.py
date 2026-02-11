"""
Simplified version of SESSION-041/iterator-demo.py

ORIGINAL: Uses a separate Gensquare_iterator wrapper class that just
delegates __next__ to the generator, plus type(N) != int check.
SIMPLIFIED: Removes unnecessary wrapper class, uses isinstance(),
yields directly from __iter__ (Python's standard iterator protocol).
"""


class Gensquare:
    def __init__(self, N: int):
        if not isinstance(N, int):
            raise TypeError("N must be int")
        if N <= 0:
            raise ValueError("N must be positive")
        self.N = N

    def __iter__(self):
        for i in range(self.N):
            yield i ** 2


# This loop prints squares of all numbers from 0 to 7
for x in Gensquare(8):
    print(x)
