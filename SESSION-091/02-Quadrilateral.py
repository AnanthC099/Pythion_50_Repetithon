class Point2D: 
    def __init__(self, init_x:float, init_y:float): 
        acceptable_types = [int, float]
        if type(init_x) not in acceptable_types or type(init_y) not in acceptable_types:
            raise TypeError('Point coordinates must be a numerical data')
        self.x = init_x 
        self.y = init_y 

    def distance(self, other) -> float: 
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
 
    def show(self): 
        print(f'({self.x}, {self.y})')

P1 = Point2D(3.5, 6.7) # P1.__dict__    {'x':3.5, 'y':6.7}
P2 = Point2D(-2.1, 5.9)

d = P1.distance(P2)

P1.show() 
P2.show() 
print('Distance between P1 and P2:', d)

#------------------------POINT2D DONE-------------------------------------

#-----------------------QUADRILATERAL-------------------------------------

class Quadrilateral: 
    def __init__(self, A:Point2D, B:Point2D, C:Point2D, D:Point2D): 
        if type(A) is not Point2D or type(B) is not Point2D or type(C) is not Point2D or type(D) is not Point2D: 
            raise TypeError("Bad type for initialial data, all data must be Point2D objects")
        
        self.A = A 
        self.B = B 
        self.C = C 
        self.D = D 
        
        self.AB = A.distance(B)
        self.BC = B.distance(C)
        self.CD = C.distance(D) 
        self.DA = D.distance(A)

        if self.AB <= 0.0 or self.BC <= 0.0 or self.CD <= 0.0 or self.DA <= 0.0: 
            raise ValueError('Input points do not form a valid quadrilateral')

        if (
            (self.AB + self.BC + self.CD <= self.DA) or 
            (self.BC + self.CD + self.DA <= self.AB) or 
            (self.CD + self.DA + self.AB <= self.BC) or 
            (self.DA + self.AB + self.BC <= self.CD)
        ): 
            raise ValueError('Input points do not form a valid quadrilateral')

    def perimeter(self) -> float: 
        return self.AB + self.BC + self.CD + self.DA 

    def area(self) -> float: 
        s = self.perimeter() / 2.0
        return ((s - self.AB) * (s - self.BC) * (s - self.CD) * (s - self.DA) ) ** 0.5


U = Point2D(5.4, 3.2)
V = Point2D(2.5, 1.9)
W = Point2D(2.4, 7.5)
Z = Point2D(7.9, 9.1)

Q = Quadrilateral(U, V, W, Z)
P = Q.perimeter() 
A = Q.area() 

print(f'PERIMETER:{P}, AREA:{A}')

# Q = Quadrilateral(Point2D(5.4, 3.2), Point2D(2.5, 1.9), Point2D(2.4, 7.5), Point2D(7.9, 9.1))