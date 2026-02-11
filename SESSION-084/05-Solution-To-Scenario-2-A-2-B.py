# Scenario 2 - A : Modify global variable being inside the function 
# by an independent value (i.e. the updated value of global variable 
# is not derived from the current value of global variable )

# BEFORE 
N = 100
def f(): 
    N = 500  # Global N is not modified instead local N was created 
f() 

# AFTER 

N = 100 
def f(): 
    global N 
    N = 500 
print("global: Value of global N before call to f():", N)
f() 
print("global: Value of global N after call to f():", N)

# Scenario 2 - B 

# BEFORE 

'''
# Modify global N from local scope based on current value of global N 
N = 100 
def f(): 
    N = N + 1  # UnboundLocalError 
f() 
''' 

# AFTER 
N = 100 
def f(): 
    global N 
    N = N + 1 
print("global:Value of N before call to f():", N)
f() 
print("global:Value of N after call t f():", N)