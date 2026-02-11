# Prep - code 
def outer(): 
    N = 100 
    def inner(): 
        print('inner():N:', N)  # function named inner() is dependent on function named 
                                # outer() for resolution of its refernce to variable N 
                                # This dependency is fulfilled by the outer function 
                                # even before the inner function is defined 
    inner() 
outer() 

#----------------------------------------------------------------
# Next code fragment 

def outer(): 
    def inner(): 
        print('inner():N:', N)
    N = 100 
    inner()
outer() 

#-----------------------------------------------------------------
# NameError: Free variable version 

def outer(): 
    def inner(): 
        print('inner():N:', N) 
    inner() 
    N = 100 
outer() 

# You are already aware of one version of NameError exception: 
# If you access undefined (non-existent) variable name v in RHS sense 
# then Python raises the NameError exception emitting the error message 
# that : the name 'v' is not defined 

#------------------------------------------------------------------------

def outer(): 
    N = 100 
    def inner(): 
        print('inner():N:', N)
    del N 
    inner() 
outer() 


