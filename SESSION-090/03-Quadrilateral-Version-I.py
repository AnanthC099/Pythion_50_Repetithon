class Quadrilateral: 
    def __init__(self, init_s1, init_s2, init_s3, init_s4): 
        self.s1 = init_s1 
        self.s2 = init_s2 
        self.s3 = init_s3 
        self.s4 = init_s4 

    def perimeter(self): 
        return self.s1 + self.s2 + self.s3 + self.s4


Q1 = Quadrilateral(3.5, 2.7, 4.9, 7.1)
Q2 = Quadrilateral(5.3, 6.8, 2.9, 5.5)

print('Q1.__dict__:', Q1.__dict__)
print('Q2.__dict__:', Q2.__dict__)

p_Q1 = Q1.perimeter()  # Quadrilateral.perimeter(Q1)
p_Q2 = Q2.perimeter()

print(f'Perimeter(Q1):{p_Q1}, Perimeter(Q2):{p_Q2}')