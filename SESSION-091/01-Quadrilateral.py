class Quadrilateral: 
    def __init__(self, init_s1:float, init_s2:float, init_s3:float, init_s4:float): 
        acceptable_types = [int, float]
        if (type(init_s1) not in acceptable_types or 
            type(init_s2) not in acceptable_types or 
            type(init_s3) not in acceptable_types or 
            type(init_s4) not in acceptable_types): 
            raise TypeError('All sides of quadrilateral must be int or float objects')
        
        if init_s1 <= 0.0 or init_s2 <= 0.0 or init_s3 <= 0.0 or init_s4 <= 0.0: 
            raise ValueError('All sides of quadrilateral must be positive numbers')

        if  (
            (init_s1 + init_s2 + init_s3 <= init_s4) or 
            (init_s2 + init_s3 + init_s4 <= init_s1) or 
            (init_s3 + init_s4 + init_s1 <= init_s2) or 
            (init_s4 + init_s1 + init_s2 <= init_s3)
        ):
            raise ValueError('Sum of any three sides of quadrilateral must be greater than that of the third')
        
        self.s1, self.s2, self.s3, self.s4 = init_s1, init_s2, init_s3, init_s4

    def perimeter(self) -> float: 
        return self.s1 + self.s2 + self.s3 + self.s4 

    def area(self) -> float: 
        s = self.perimeter() / 2.0 
        return ((s - self.s1) * (s - self.s2) * (s - self.s3) * (s - self.s4)) ** 0.5


Q1 = Quadrilateral(3.4, 5.6, 3.1, 6.8)
area_Q1 = Q1.area() # Quadrilateral.area(Q1)
perimeter_Q1 = Q1.perimeter() # Quadrilateral.perimeter(Q1)

print(f'Area:{area_Q1}, Perimeter:{perimeter_Q1}')