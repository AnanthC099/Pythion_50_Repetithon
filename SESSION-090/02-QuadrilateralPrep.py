class Quadrilateral: 
    def __init__(self): 
        print('self.__dict__:', self.__dict__)
        self.s1 = 10.10 
        print('self.__dict__:', self.__dict__)
        self.s2 = 6.8
        print('self.__dict__:', self.__dict__)
        self.s3 = 5.6 
        print('self.__dict__:', self.__dict__)
        self.s4 = 2.8 
        print('self.__dict__:', self.__dict__)
        print('id(self):', id(self))

Q1 = Quadrilateral() 
print('id(Q1):', id(Q1))
print('Q1.__dict__:', Q1.__dict__)

Q1.quad_type = 'Scalen'

print('Q1.__dict__:', Q1.__dict__)

Q1.s3 = 8.6 

print('Q1.__dict__:', Q1.__dict__)

del Q1.quad_type

print('Q1.__dict__:', Q1.__dict__)

print(Q1.s1)
print(Q1.s2)
print(Q1.s3)
print(Q1.s4)