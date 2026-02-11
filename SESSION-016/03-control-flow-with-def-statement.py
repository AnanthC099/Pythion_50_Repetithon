print('Start of program')
a = 10
b = 20

def testFunction(x, y):
    print('Entered testFunction()') 
    z1 = x + y
    z2 = x - y
    print(z1)
    print(z2)
    print('Leaving testFunction()')

c = a + b
print(a)
print(b)
print(c)
testFunction(100, 200) 
print('End of program') 
