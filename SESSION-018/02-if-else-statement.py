print('Start of program')

num = 100
result = num
a = int(input('Enter an integer:'))

if a > 0:
    print('Input number is positive')
    result = num / a
else:
    print('Input number is negative or zero')
    result = num * a

print('Result:', result)
print('End of program') 
