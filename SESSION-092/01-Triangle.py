class Point2D: 
    def __init__(self, init_x:float, init_y:float): 
        acceptable_types = [int, float]
        if type(init_x) not in acceptable_types or type(init_y) not in acceptable_types:
            raise TypeError('Bad type: initialization data')
        self.x, self.y = init_x, init_y 

    def distance(self, other) -> float: 
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def show(self) -> None:  
        print(f'({self.x}, {self.y})')


class Triangle: 
    def __init__(self, A:Point2D, B:Point2D, C:Point2D): 
        if type(A) != Point2D or type(B) is not Point2D or type(C) is not Point2D: 
            raise TypeError('Bad type for initialization data')
        self.A, self.B, self.C = A, B, C 
        self.AB, self.BC, self.CA = A.distance(B), B.distance(C), C.distance(A)
        if (self.AB <= 0.0 or self.BC <= 0.0 or self.CA <= 0.0 or 
            self.AB + self.BC <= self.CA or 
            self.BC + self.CA <= self.AB or 
            self.CA + self.AB <= self.BC): 
            raise ValueError('Given three points do not form a valid triangle')

    def perimeter(self) -> float: 
        return self.AB + self.BC + self.CA 

    def area(self) -> float: 
        s = self.perimeter() / 2.0 
        return (s * (s - self.AB) * (s - self.BC) * (s - self.CA)) ** 0.5

    def triangle_type(self) -> str: 
        if self.AB == self.BC and self.BC == self.CA and self.CA == self.AB: 
            return "Equilateral"
        elif self.AB == self.BC or self.BC == self.CA or self.CA == self.AB: 
            return "Isosceles"
        else: 
            return "Scalene"

# Write a client side to rigorously test the code
# Try to generate intelligent boundary cases

#-----------------------CLIENT SIDE CODE-----------------------------------

# Scalene triangle
P1 = Point2D(0.0, 0.0)
P2 = Point2D(4.0, 0.0)
P3 = Point2D(1.0, 3.0)

T1 = Triangle(P1, P2, P3)
print('--- Scalene Triangle ---')
print(f'Perimeter: {T1.perimeter()}')
print(f'Area: {T1.area()}')
print(f'Type: {T1.triangle_type()}')

# Equilateral triangle (side length 2)
A = Point2D(0.0, 0.0)
B = Point2D(2.0, 0.0)
C = Point2D(1.0, 3**0.5)

T2 = Triangle(A, B, C)
print('\n--- Equilateral Triangle ---')
print(f'Perimeter: {T2.perimeter()}')
print(f'Area: {T2.area()}')
print(f'Type: {T2.triangle_type()}')

# Isosceles triangle
X = Point2D(0.0, 0.0)
Y = Point2D(4.0, 0.0)
Z = Point2D(2.0, 5.0)

T3 = Triangle(X, Y, Z)
print('\n--- Isosceles Triangle ---')
print(f'Perimeter: {T3.perimeter()}')
print(f'Area: {T3.area()}')
print(f'Type: {T3.triangle_type()}')

# Right triangle (3-4-5)
R1 = Point2D(0.0, 0.0)
R2 = Point2D(3.0, 0.0)
R3 = Point2D(0.0, 4.0)

T4 = Triangle(R1, R2, R3)
print('\n--- Right Triangle (3-4-5) ---')
print(f'Perimeter: {T4.perimeter()}')
print(f'Area: {T4.area()}')
print(f'Type: {T4.triangle_type()}')

#-----------------------BOUNDARY CASES-------------------------------------

# Collinear points - should raise ValueError
try:
    T_bad = Triangle(Point2D(0.0, 0.0), Point2D(1.0, 1.0), Point2D(2.0, 2.0))
    print('\nERROR: Collinear points should have raised ValueError')
except ValueError as e:
    print(f'\nCollinear points correctly rejected: {e}')

# Bad type - should raise TypeError
try:
    T_bad = Triangle(Point2D(0.0, 0.0), Point2D(1.0, 1.0), "not a point")
    print('ERROR: Bad type should have raised TypeError')
except TypeError as e:
    print(f'Bad type correctly rejected: {e}')

# Duplicate points - should raise ValueError
try:
    T_bad = Triangle(Point2D(1.0, 1.0), Point2D(1.0, 1.0), Point2D(3.0, 4.0))
    print('ERROR: Duplicate points should have raised ValueError')
except ValueError as e:
    print(f'Duplicate points correctly rejected: {e}')