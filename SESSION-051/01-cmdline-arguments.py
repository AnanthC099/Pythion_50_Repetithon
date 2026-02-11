import sys 

print('type(sys.argv):', type(sys.argv)) 
print('sys.argv:', sys.argv)
print('------------------------------------------------------')
print('Print all command line arguments using for loop')
for word in sys.argv: 
    print(word)
print('------------------------------------------------------')
print('Print all command line arguments using while loop')
i = 0 
while i < len(sys.argv): 
    print('sys.argv[', i, ']:', sys.argv[i])
    i = i + 1 
print('------------------------------------------------------')