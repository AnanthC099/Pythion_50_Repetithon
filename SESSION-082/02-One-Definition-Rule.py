'''
A variable name can be defined only once in a given scope. 
In other words there cannot be more than one definition of 
variable in any given scope. 

If you change the scope the variable names created in other 
scopes can be recreated for the changed scope. 

For example, if we define N in global scope then it can be 
RE-ASSIGNED but cannot be REDEFINED in the global scope. 

But if we define two functions, f1() and f2() where f2() 
is a nested function f1() then we can create a new version 
of N in both f1() and f2(). Because defining new function 
creates a new scope and we are allowed to recreate N in newly 
created scope. 

Therefore while the control flow is in function f2() three versions 
of N are simultaneously existing. 

With reference to the following code 
1) Global version of N valued 100 
2) Local variable N of function f1() valued 200 
3) Local variable N of function f2()  valued 300 
'''

N = 100 
print('global symbol table:globals():', globals())
def f1(): 
    N = 200 
    print('local symbol table of f1():', locals())
    def f2(): 
        N = 300 
        print('local symbol table of f2():', locals())
        input('Enter any key to continue....')
    f2() 
f1() 