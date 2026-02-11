# Code Fragment 1 

def outer(): 
    num = 500 

    def inner(): 
        print('inner():Function entered')
        print('inner():num:', num)
        print('inner():Function leaving')
    
    print('outer():type(inner):', type(inner))
    print('outer():id(inner):', id(inner))

    return inner

X = outer() 
print('global():type(X):', type(X))
print('global():id(X):', id(X))

print('global():Putting call operator on global variable X')
X()
print('global():End of program')
