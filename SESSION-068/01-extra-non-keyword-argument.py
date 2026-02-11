def testFunction(a, b): 
    print(a, b)

testFunction(100, 200)
testFunction('Hello', 'World')

# A call to testFunction() will raise an exception 
# if we send less than two or more than two actual parameters
# Why? Because testFunction() accepts two formal parameters
# therefore, we must give two actual parameters 

# Lets examine the behaviour of print() function 

# print() with zero actual parameters 
print()     # No error 

# print() with one actual parameter 
print(10)   # No error 

# print() with two actual parameters 
print(100, 200)                         # No error 
print([100, 200, 300], (-1, -2, -3))    # No error 

# print() with three actual paremeters 
print(100, 200, 300)                                            # No error 
print('a', 'b', 'c')                                            # No error 
print([100, 200, 300], (-1, -2, -3), {'p': True, 'q': False})   # No error 

# How is formal parameter list of print() function written? 
'''
def print() 
    LOGIC 

This will work with zero parameters but not with 1, 2, 3 

def print(a): 
    LOGIC 

This will work with one parameter but not with 0, 2, 3 

def print(a, b): 
    LOGIC 

This will work with two parameters but not with 0, 1 and three 

def print(a, b, c): 
    LOGIC 

This will work with three parameters but not with 0, 1 and 2. 
'''

'''
print() function has a unique capacity that many other functions do not have! 
print() function can accept different NUMBER OF actual parameters per call. 
Like other functions print() is defined only once yet it can accept different 
number of actual parameters per call. 

Such function are technically known as VARIADIC FUNCTION. 
''' 

def myVariadicFunction(*myParameter): 
    print('----Entered myVariadicFunction-----')
    print(myParameter)
    print(f'type(myParameter):{type(myParameter)}')
    print('Accessing actual parameters individually')
    for x in myParameter: 
        print(x) 
    print('----Leaving myVariadicFunction----')


# Like print() function you can send different number of parameters to myVariadicFunction() 
# Zero parmaeters 
myVariadicFunction() 

# One parameter 
myVariadicFunction(10)

# Two parameters 
myVariadicFunction(10, 20)

# Three parameters 
myVariadicFunction(10, 20, 30)
