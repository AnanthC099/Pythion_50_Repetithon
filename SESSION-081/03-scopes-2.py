print('start of program')                           # global 
print('This code demonstrates enclosing scope')     # global 
def f1():                                           # global
    L = [10, 20, 30, 40]                            # local wrt f1() 
    for x in L:                                     # local wrt f1() 
        print(x)                                    # local wrt f1() 
    def f2():                                       # local wrt f1() 
        D = {'p' : True, 'q': False}                # local wrt f2(), enclosing with f1()
        def f3():                                   # local wrt f2(), enclosing with f1() 
            S = {100, 200, 300}                     # local wrt f3(), enclosing with f1(), enclosing with f2()
            for x in S:                             # local wrt f3(), enclosing with f1(), enclosing with f2() 
                print(x**2)                         # local wrt f3(), enclosing with f1(), enclosing with f2()
            
            for x in S:                             # local wrt f3(), enclosing with f1(), enclosing with f2()
                if x > 100:                         # local wrt f3(), enclosing with f1(), enclosing with f2()
                    y = x + 400                     # local wrt f3(), enclosing with f1(), enclosing with f2()           
                    z = y ** 2                      # local wrt f3(), enclosing with f1(), enclosing with f2()
                    print(z)                        # local wrt f3(), enclosing with f1(), enclosing with f2()
            
        f3()                                        # local wrt f2(), enclosing with f1()
        for (key, val) in D.items():                # local wrt f2(), enclosing with f1()
            print(key, val)                         # local wrt f2(), enclosing with f1()
    f2()                                            # local wrt f1() 
    print(L)                                        # local wrt f1() 
f1()                                                # global 
print('End of program')                             # global 