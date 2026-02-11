def mySquareRoot(x:float): 
    '''
    @x : must be a non-negative floating point number 
    '''

    # Check if type(x) is int or float 
    # If not then raise TypeError exception 
    if type(x) is not int and type(x) is not float: 
        raise TypeError('Bad type for input parameter x: x must be int or float')

    if x < 0.0: 
        raise ValueError('Bad value for x: x must be 0 or positive')

    print('LOGIC of computing square root')
    return x ** 0.5 


result = mySquareRoot(4.0)
print(f'Result:{result}')

result = mySquareRoot("Hello")
# mySquareRoot('Hello') will trigger a TypeError 
# exception. Because we have not handled the exception 
# the program will terminate here and the next lines 
# will not be exectued 

result = mySquareRoot(9.0)
print(f'Result:{result}')

print('----END OF PROGRAM----')


