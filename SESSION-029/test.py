class Date:
    day = 30
    month = 9
    year = 2025

D = Date()
print(D.day, D.month, D.year)
print('D.__dict__:', D.__dict__)
print('Date.__dict__:', Date.__dict__)

