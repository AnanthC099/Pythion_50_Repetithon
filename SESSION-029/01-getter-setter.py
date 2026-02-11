class Date:
    def __init__(self, init_day, init_month, init_year):
        print('Entered Date.__init__():id(self):', id(self))
        print('self.__dict__:', self.__dict__)
        self.day = init_day
        self.month = init_month
        self.year = init_year
        print('Leaving Date.__init__():self.__dict__:', self.__dict__)


    def get_day(self):
        print('get_day():id(self):', id(self))
        print('self.__dict__:', self.__dict__)
        return self.day


    def set_day(self, new_day):
        print('set_day():BEFORE:id(self):', id(self))
        print('BEFORE:self.__dict__:', self.__dict__)
        self.day = new_day
        print('AFTER:self.__dict__:', self.__dict__)
        print('set_day():AFTER:id(self):', id(self))

D = Date(30, 9, 2025)
print('id(D):', id(D))
print('D.__dict__:', D.__dict__)
d = D.get_day() # Date.get_day(D)
print('d:', d)

D.set_day(25) # Date.set_day(D, 25)
d = D.get_day()
print('d:', d)
