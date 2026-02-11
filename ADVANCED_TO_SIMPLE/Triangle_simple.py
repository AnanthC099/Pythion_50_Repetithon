"""
Simplified version of Triangle.py (SESSION-092/01-Triangle.py)

ORIGINAL (Advanced): Used 'type(x) is not in acceptable_types' (syntax bug),
inconsistent type checks ('!=' vs 'is not'), separate Point2D class
with same bug.

SIMPLIFIED: Uses isinstance() for type checking, fixes bugs,
cleaner structure, fixes "Scalen" typo to "Scalene".
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


class Triangle:
    def __init__(self, A: Point2D, B: Point2D, C: Point2D):
        if not all(isinstance(p, Point2D) for p in (A, B, C)):
            raise TypeError("All vertices must be Point2D objects")

        self.A, self.B, self.C = A, B, C
        self.AB = A.distance(B)
        self.BC = B.distance(C)
        self.CA = C.distance(A)

        sides = [self.AB, self.BC, self.CA]
        if any(s <= 0 for s in sides):
            raise ValueError("Side lengths must be positive")
        if (self.AB + self.BC <= self.CA or
            self.BC + self.CA <= self.AB or
            self.CA + self.AB <= self.BC):
            raise ValueError("Points do not form a valid triangle")

    def perimeter(self) -> float:
        return self.AB + self.BC + self.CA

    def area(self) -> float:
        s = self.perimeter() / 2.0
        return (s * (s - self.AB) * (s - self.BC) * (s - self.CA)) ** 0.5

    def triangle_type(self) -> str:
        if self.AB == self.BC == self.CA:
            return "Equilateral"
        elif self.AB == self.BC or self.BC == self.CA or self.CA == self.AB:
            return "Isosceles"
        else:
            return "Scalene"


# --- Testing ---
A = Point2D(0, 0)
B = Point2D(3, 0)
C = Point2D(0, 4)

t = Triangle(A, B, C)
print(f"Vertices: {t.A}, {t.B}, {t.C}")
print(f"Sides: AB={t.AB}, BC={t.BC}, CA={t.CA}")
print(f"Perimeter: {t.perimeter()}")
print(f"Area: {t.area()}")
print(f"Type: {t.triangle_type()}")
