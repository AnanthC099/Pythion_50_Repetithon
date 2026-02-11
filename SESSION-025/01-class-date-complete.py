class Date:
    def __init__(self): 
        print('Entered Date.__init__()')
        print('type(self):', type(self))
        print('id(self):', id(self))
        print('Leaving Date.__init__()')

D1 = Date()
print('type(D1):', type(D1))
print('id(D1):', id(D1))
D2 = Date()
print('type(D2):', type(D2))
print('id(D2):', id(D2))

