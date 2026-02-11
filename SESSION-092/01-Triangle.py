class Point2D: 
    def __init__(self, init_x:float, init_y:float): 
        acceptable_types = [int, float]
        if type(init_x) is not in acceptable_types or type(init_y) is not in acceptable_types: 
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
        return ((s - self.AB) * (s - self.BC) * (s - self.CA)) ** 0.5 

    def triangle_type(self) -> str: 
        if self.AB == self.BC and self.BC == self.CA and self.CA == self.AB: 
            return "Equilateral"
        elif self.AB == self.BC or self.BC == self.CA or self.CA == self.AB: 
            return "Isosceles"
        else: 
            return "Scalen"

# Write a client side to rigorously test the code 
# Try to generate intelligent boundary cases         