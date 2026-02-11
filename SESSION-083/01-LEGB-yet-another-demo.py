N = 10 
def f1(): 
    N = 100 
    def f2(): 
        N = 1000 
        def f3(): 
            N = 10000 
            print(N) 
        f3() 
    f2() 
f1() 