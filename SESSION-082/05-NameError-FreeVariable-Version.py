# NameError : Free Variable Version 

# Without error 
def f(): 
    n = 100 
    def g(): 
        print(n) 
    g() 
f()

# Without error 

def f(): 
    def g(): 
        print(n) 
    n = 100 
    g() 
f() 

# With error 1 
def f(): 
    def g(): 
        print(n)  # NameError: Free Variable 
    g() 
    n = 100 
f() 

# With error 2 
def f(): 
    n = 100 
    def g(): 
        print(n) # NameError : Free Variable 
    del n 
    g() 
f() 
