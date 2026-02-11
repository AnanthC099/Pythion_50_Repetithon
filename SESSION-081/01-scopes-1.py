# This file will deminstrate global and local scopes 

L = [10, 20, 30, 40, 50]                # global scope 
for x in L:                             # global scope 
    print(x)                            # global scope 

def my_func_1():                        # global scope 
    D = {'a': 100, 'b': 200, 'c': 300}  # local scope wrt my_func_1()
    for (key, value) in D.items():      # local scope wrt my_func_1()     
        if value > 100:                 # local scope wrt my_func_1()  
            print(key, value)           # local scope wrt my_func_1()  


def my_func_2():                                # global scope 
    L = [100, 200, 300, 400, 500, 600, 700]     # local scope wrt my_func_2()
    M = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]     # local scope wrt my_func_2()
    result = []                                 # local scope wrt my_func_2()
    for p in L:                                 # local scope wrt my_func_2()
        for q in M:                             # local scope wrt my_func_2()
            T = (p, q):                         # local scope wrt my_func_2()
            result.append(T)                    # local scope wrt my_func_2()
    print(result)                               # local scope wrt my_func_2()

my_func_1()     # global scope 
my_func_2()     # global scope 

class Date:     # global scope 
    def __init__(self, init_day, init_month, init_year):    # local scope wrt class Date (class namespace)
        self.day = init_day         # local scope wrt class method __init__()
        self.month = init_month     # local scope wrt class method __init__()
        self.year = init_year       # local scope wrt class method __init__()

    def getDay(self):               # local scope wrt class Date 
        return self.day             # local scope wrt class method getDay() 

    def setDay(self, newDay):       # local scope wrt class Date 
        self.day = newDay           # local scope wrt class method setDay()


# Stats: Module 1, functions - 2, class - 1, 3 class methods 
# Total number of symbol tables == 8  
# We have a module scope, 2 scopes introduced by two functions and 1 scope introduced by 1 class 

# GOLDEN RULE: Every statement in each Python source file must belong to a global scope 
# or a local scope of stand-alone function or a local scope of class method or a local scope of class 

# This is known as a primary scope of that statement 
# Every statement must be in 
# 1) Global scope : Inside module, outside all functions, all classes 
# 2) Local scope of a function : Inside module, and inside function which is defined outside of all classes
# 3) Local scope of a function inside class : Inside moulde, inside a function which inside a class 
# 4) Local scope of class : Inside module, inside class but outside all functions in a class 

class Test:     # global scope 
    a = 10      # local scope of class (class namespace = class madhye define keleli variables)
    b = 20      # local scope of class 
    def my_method(self):    # local scope of class 
        m = 100     # local with respect to method inside class 
        n = 200     # local with respect to method inside class 
