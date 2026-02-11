m = 100 # m will be created in global symbol table 

def f1(): 
    n = 200     # n will be created in local symbol table of f1() 

    def f2(): 
        k = 300     # k will be created in local symbol table of f2() 

    f2() 

f1()

'''
Variable name used on LHS for the first time in created in the symbol 
of table scope of its statement 

GENERALIZED TREATMENT OF LHS SENSE USE OF VARIABLE NAME 
Whenever a variable name is used on LHS, for definition or for reassignment, 
symbol table associated with scope of the statement using variable name is 
used. Rest of the algorithm follows assignment statement algorithm. 
'''