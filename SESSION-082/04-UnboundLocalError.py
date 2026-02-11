# UnboundLocalError Case 1 
n = 100 
def f(): 
    print(n) 
    n = 200 
f() 
#----------------------------------
# UnboundLocalError Case 2 
n = 100 
def f(): 
    n = n + 1
f()  
#-----------------------------------

