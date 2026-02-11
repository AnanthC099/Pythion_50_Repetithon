print('START OF PROGRAM')

class Date:
    def __init__(self):
        print('VALUE PART OF OBJECT AT ENTER:')
        print(self.__dict__)
        print('-------------------------------')
        print('FILLING DATA IN OBJECT:')
        self.day = 24
        self.month = 9
        self.year = 2025
        print('-------------------------------')
        print('VALUE PART OF OBJECT AT LEAVING:')
        print(self.__dict__)
        print('-------------------------------')
        print('LEAVING Date.__init__()')

D1 = Date()
print('D1.__dict__:', D1.__dict__)
print('END OF PROGRAM') 

