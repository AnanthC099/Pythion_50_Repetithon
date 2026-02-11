'''
General conversion from lambda expression to def statement 

lambda x1, x2, ..., xn : EXPR(x1, x2, ...., xn)

== 

def func(x1, x2, ..., xn): 
    return EXPR(x1, x2, ..., xn)
'''

(lambda n : n ** 2)

# is equivalent to 

def func(n): 
    return n ** 2 

(lambda x, y, z: x*2 + y*3 + z*4) 

# is equivalent to 

def func(x, y, z): 
    return x*2 + y*3 + z*4


(lambda x, y, z=1.5 : x + y * z) 

# is equivalent to 

def func(x, y, z=1.5): 
    return x + y * z 

(lambda *args : print(args))

# is equivalent to 

def func(*args): 
    return print(args) 

#------------------------------------------------------------------