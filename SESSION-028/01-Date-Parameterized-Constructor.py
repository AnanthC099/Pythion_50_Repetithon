class Date:
    def __init__(self, init_day, init_month, init_year):
        self.day = init_day
        self.month = init_month
        self.year = init_year


today = Date(26, 9, 2025)
print('today.__dict__:', today.__dict__)
examDate = Date(15, 11, 2025)
print('examDate.__dict__:', examDate.__dict__)
yearEnd = Date(31, 12, 2025)
print('yearEnd.__dict__:', yearEnd.__dict__)
