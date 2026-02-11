'''
Characterize implicit state saving question
''' 

def outer(): 
    N = 100 
    def inner(): 
        print('inner():N:', N)
    return inner 

X = outer() 
X() 

'''
Characterizing problem: 
    We have defined a function named outer() which defines two local variables. 
    1) N        ->  Naming integer object 100 
    2) inner    ->  Naming a nested function object 

    Inside inner() function, outer() functions local variable N is used on RHS 
    making use of LEGB scope rule. 

    But we are not calling inner() function as a part of execution of outer() function, 
    rather we are returning inner() function to the caller of the outer function. 

    Caller of outer() function is saving the return value in global variable named X. 
    When X() is called a function which went by the name 'inner()' while the outer() 
    function was executing will be called. 

    Because the control is not in the outer function its symbol table is empty. 
    How does reference to N made in the call of X() gets resolved? 
''' 

#----------------------------------------------------------------------------------------
# Pattern #1 
def outer(): 
    N = 100 
    def inner(): 
        print('inner():N:', N)
    inner() 
outer() 
#------------------------------------------------------------------------------------------------------
# Pattern 2 
def outer(): 
    N = 100 
    def inner(): 
        print('inner():N:', N)
    return inner 
X = outer() 
X() 
#------------------------------------------------------------------------------------------------------------

