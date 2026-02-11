"""
Simplified version of SESSION-081/01-scopes-1.py

ORIGINAL: Line 20 has a syntax error - 'T = (p, q):' (extra colon).
Also mixes scope teaching with class definition.
SIMPLIFIED: Fixes the syntax error, same scope demonstration.
"""

# Global scope
L = [10, 20, 30, 40, 50]
for x in L:
    print(x)


def my_func_1():
    # Local scope of my_func_1
    D = {"a": 100, "b": 200, "c": 300}
    for key, value in D.items():
        if value > 100:
            print(key, value)


def my_func_2():
    # Local scope of my_func_2
    L = [100, 200, 300, 400, 500, 600, 700]
    M = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    result = []
    for p in L:
        for q in M:
            T = (p, q)  # Fixed: removed extra colon
            result.append(T)
    print(result)


my_func_1()
my_func_2()


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def set_day(self, new_day):
        self.day = new_day
