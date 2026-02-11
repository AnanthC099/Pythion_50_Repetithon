class Quadrilateral: 
    def __init__(self): 
        print('----Entered Quadrilateral.__init__()----')
        print('type(self):', type(self))
        print('id(self):', id(self))
        print('----Leaving Quadrilateral.__init__()----')

Q1 = Quadrilateral() 
Q2 = Quadrilateral() 

print(f'type(Q1):{type(Q1)}, id(Q1):{id(Q1)}')
print(f'type(Q2):{type(Q2)}, id(Q2):{id(Q2)}')



