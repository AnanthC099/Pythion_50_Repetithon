# Scenario 1 

N = 100 
def f(): 
    N = 200 
    def g(): 
        print('N:', N)  # Global N is hidden by enclosing scope's N 
    g() 
f() 

#--------------------------

# Scenario 2 
# You want to update the value of global variable 
# being in the local scope of a function 

# Scenario 2 - A 

N = 100 
def f(): 
    N = 500     # No global N is modified instead local N is created 
f() 

# Scenario 2 - B 
N = 100 
def f(): 
    N = N + 1   # Not only global variable did not get modified but 
                # UnboundLocalError exception got generated 
f() 

# Karne anek - uttar ek 