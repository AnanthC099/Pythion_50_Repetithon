"""
Simplified version of SESSION-091/02-Quadrilateral.py

ORIGINAL: Uses 'type(A) is not Point2D' repeated 4 times in a long 'or' chain,
Point2D uses 'type(x) not in acceptable_types'.
SIMPLIFIED: Uses isinstance() with tuple, cleaner validation.
"""


class Point2D:
    def __init__(self, x: float, y: float):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be int or float")
        self.x, self.y = x, y

    def distance(self, other) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Quadrilateral:
    def __init__(self, A: Point2D, B: Point2D, C: Point2D, D: Point2D):
        if not all(isinstance(p, Point2D) for p in (A, B, C, D)):
            raise TypeError("All points must be Point2D objects")

        self.A, self.B, self.C, self.D = A, B, C, D
        self.AB = A.distance(B)
        self.BC = B.distance(C)
        self.CD = C.distance(D)
        self.DA = D.distance(A)

        sides = [self.AB, self.BC, self.CD, self.DA]
        if any(s <= 0 for s in sides):
            raise ValueError("Points do not form a valid quadrilateral")

        for i in range(4):
            if sum(sides) - sides[i] <= sides[i]:
                raise ValueError("Points do not form a valid quadrilateral")

    def perimeter(self) -> float:
        return self.AB + self.BC + self.CD + self.DA

    def area(self) -> float:
        s = self.perimeter() / 2.0
        return ((s - self.AB) * (s - self.BC) * (s - self.CD) * (s - self.DA)) ** 0.5


# --- Testing ---
U = Point2D(5.4, 3.2)
V = Point2D(2.5, 1.9)
W = Point2D(2.4, 7.5)
Z = Point2D(7.9, 9.1)

Q = Quadrilateral(U, V, W, Z)
print(f"Perimeter: {Q.perimeter()}, Area: {Q.area()}")
