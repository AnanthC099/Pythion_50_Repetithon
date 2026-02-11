print('Start of program')

print('PART 1 - START')
L = [2, 5, 8, 11, 17, 25, 60]
for x in L:
    if x % 7 == 0:
        break
    print('Current Value of x:', x)
else:
    print('The for loop executed without break statement')
print('PART 1 - END')

print('PART 2 - START')
L = [10, 20, 30, 40, 49, 55, 60, 69]
for x in L:
    if x % 7 == 0:
        break
    print('Current Value of x:', x)
else:
    print('Control flow will not come here')
print('PART 2 - END')

print('End of program') 

