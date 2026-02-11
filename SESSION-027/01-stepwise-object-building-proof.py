print('START OF PROGRAM')

class Date:
    def __init__(self):
        print('Entered Date.__init__()') 
        print('Initial state of value component:', self.__dict__) 
        self.day = 25
        print('State of value component after self.day = 25:', self.__dict__)
        self.month = 9
        print('State of value component after self.month = 9:', self.__dict__)
        self.year = 2025
        print('State of value component after self.year = 2025:', self.__dict__)
        print('Leaving Date.__init__()')

print('ABOUT TO CREATE NEW OBJECT OF DATE AND NAME IT AS D')
D = Date()
print('PRINTING VALUE COMPONENT OF CONSTRUCTED OBJECT D:', D.__dict__)
print('END OF PROGRAM') 
