"""
Simplified version of Vector3D.py

ORIGINAL (Advanced): Used 'type(x) is not in acceptable_types' (syntax bug),
repetitive type checking with 'type() is not' in every method,
no operator overloading.

SIMPLIFIED: Uses isinstance() for clean type checking, fixes the bug,
removes redundant self-type checks, adds __repr__ for easy printing.
"""


class Vector3D:
    def __init__(self, x: float, y: float, z: float):
        for val in (x, y, z):
            if not isinstance(val, (int, float)):
                raise TypeError(f"Expected int or float, got {type(val).__name__}")
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"({self.x})i + ({self.y})j + ({self.z})k"

    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def subtract(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def mod(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def normalize(self):
        n = self.mod()
        if n == 0.0:
            raise ValueError("Zero vector cannot be normalized")
        return Vector3D(self.x / n, self.y / n, self.z / n)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )


# --- Testing ---
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", v1.add(v2))
print("v1 - v2:", v1.subtract(v2))
print("|v1|:", v1.mod())
print("v1 normalized:", v1.normalize())
print("v1 . v2:", v1.dot(v2))
print("v1 x v2:", v1.cross(v2))
