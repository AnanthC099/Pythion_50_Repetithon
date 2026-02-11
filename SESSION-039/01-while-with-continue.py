print('Start of program') 
L = [10, 20, 25, 30, 42, 45, 70, 75, 77, 100]
print('While loop without continue statement - START')
i = 0
while i < len(L):
    print('Value at current index:', i, 'is:', L[i])
    i = i + 1
print('While loop without continue statement - END') 


# Uncomment all the statements to experience infinite loop loop case
# After experimenting with it comment them again 
#print('The following code is written by keeping the parity with for loop')
#print('For the reasons explained in session, the following code goes in the infinite loop')
#print('Uncomment all commented statements to experiment with it')


#print('While loop with continue statement - START')
#i = 0
#while i < len(L):
#    if L[i] % 7 == 0:
#        continue
#    print('Value at current index:', i, 'is:', L[i])
#    i = i + 1
#print('While loop with continue statement - END')

print("Correct way of using while with continue")
print('while loop with continue - START')
i = 0
while i < len(L):
    if L[i] % 7 == 0:
        i = i + 1
        continue
    print('Value at index:', i, 'is:', L[i])
    i = i + 1
print('While loop with continue -END')
print('End of program') 
