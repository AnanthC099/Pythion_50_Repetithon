# Code Snippet 1 

N = 100 
print('global():N:', N)
def f(): 
    N = 200 
    print('f():N:', N) 
f() 

#------------------------------------

# Code Snippet 2 

N = 100 
def f(): 
    print("f():N:", N)
f() 

#-------------------------------------

# Code Snippet 3 

N = 100 
def f1(): 
    N = 200 
    def f2(): 
        print("f2():N:", N) 
    f2() 
f1() 

#-----------------------------------------

# Code Snippet 4 

N = 100 
def f1(): 
    print("f1():N:", N)
    def f2(): 
        print("f2():N:", N)
        print(M)
    f2() 
f1() 

#-------------------------------------------

def f(): 
    def g(): 
        def h(): 
            print(xyz)
            def k(): 
                print('In k()')
            k() 
        h()
    g() 
f() 
#-----------------------------------------   
def f(): 
    def g1(): 
        BLOCK 
    
    def g2(): 
        BLOCK 

    def g3(): 
        BLOCK 
        print(v)

    def g4(): 
        BLOCK 

    g1() 
    g2() 
    g3() 
    g4() 

f() 
#-----------------------------------------   


def f(): 
    def g1(): 
        def g2(): 
            def g3(): 
                def g4(): 
                    pass 
                g4() 
            g3() 
        g2() 
    g1() 
f() 

#-----------------------------------------          
