def outer(): 
    N = 500 
    def inner(): 
        nonlocal N 
        N = 1000 
    print('outer():N before call to inner():', N)
    inner() 
    print('outer():N after call to inner():', N)
outer()
#----------------------------------
def f1(): 
    N = 100 
    def f2(): 
        def f3(): 
            def f4(): 
                nonlocal N 
                N = 200 
            f4() 
        f3() 
    print('f1():Before call to f2():N:', N)
    f2()
    print('f1():After call to f2():N:', N)
f1() 
#----------------------------------