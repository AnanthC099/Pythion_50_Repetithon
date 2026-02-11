class Date:
    def __init__(self, init_day, init_month, init_year):
        self.day = init_day
        self.month = init_month
        self.year = init_year


    def get_day(self):
        return self.day


    def get_month(self):
        return self.month


    def get_year(self):
        return self.year


    def set_day(self, new_day):
        self.day = new_day


    def set_month(self, new_month):
        self.month = new_month


    def set_year(self, new_year):
        self.year = new_year 


    def show(self):
        print(self.day, "/", self.month, "/", self.year)


D = Date(1, 10, 2025)
D.show()
D.set_day(5)
D.show()
D.set_month(11)
D.show()
D.set_year(2026)
D.show()

dd = D.get_day()
mm = D.get_month()
yy = D.get_year()
print(dd, "/", mm, "/", yy)
