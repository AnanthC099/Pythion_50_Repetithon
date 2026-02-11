# BEFORE 

N = 100 
def outer(): 
    N = 200 
    def inner(): 
        print(N)    # global N is hidden from enclosing scope's N 
    inner() 
outer() 


# AFTER 

N = 100 
def outer(): 
    N = 200 
    def inner(): 
        global N 
        print(N) 
        N = 500 
    inner() 
outer() 