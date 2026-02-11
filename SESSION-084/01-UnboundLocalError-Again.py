N = 100 
def f(): 
    print(N)    # UnboundLocalError: Variable named N is referenced 
                # Before it is assigned. 
                # LEGB scope rule will not be applicable here. 
                # LEGB scope rule would have been applicable 
                # had N not been defined in the scope of f() 
    N = 300 
    print(N) 

f()

#------------------------------------------------------------------
# Extreme case of UnboundLocalError: Hard to spot 

N = 100 
def f(): 
    # Function f() wants to increment the value of 
    # global variable N by 1 
    N = N + 1   # UnboundLocalError: Why? Because the variable 'N' 
                # is being defined in the local scope of f() on line 21 
                # But it is accessed on RHS on the line 21 and before 
                # LHS, RHS gets executed, therefore, the error. 
f() 