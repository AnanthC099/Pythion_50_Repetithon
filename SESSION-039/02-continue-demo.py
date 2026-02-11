print('Start of program')

L = [10, 15, 20, 25, 42, 45, 70, 75, 77, 100] 

print('For loop without continue statement-START') 
for x in L:
    print('Current value of x:', x)
print('For loop without continue statement-END')

print('For loop with continue statement-START')
for x in L:
    if x % 7 == 0:
        continue
    print('Current Value of x:', x)
print('For loop with continue statement-END')

print('End of program') 


