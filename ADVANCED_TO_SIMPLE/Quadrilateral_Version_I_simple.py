"""
Simplified version of SESSION-090/03-Quadrilateral-Version-I.py

ORIGINAL: Line 18 has a bug - passes undefined 'data' arguments to
perimeter() which takes no arguments: Q1.perimeter(data, data, data)
SIMPLIFIED: Fixes the bug, clean class with correct method calls.
"""


class Quadrilateral:
    def __init__(self, s1: float, s2: float, s3: float, s4: float):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def perimeter(self) -> float:
        return self.s1 + self.s2 + self.s3 + self.s4


Q1 = Quadrilateral(3.5, 2.7, 4.9, 7.1)
Q2 = Quadrilateral(5.3, 6.8, 2.9, 5.5)

print(f"Q1 attributes: {Q1.__dict__}")
print(f"Q2 attributes: {Q2.__dict__}")

p_Q1 = Q1.perimeter()  # Fixed: removed undefined 'data' arguments
p_Q2 = Q2.perimeter()

print(f"Perimeter(Q1): {p_Q1}, Perimeter(Q2): {p_Q2}")
