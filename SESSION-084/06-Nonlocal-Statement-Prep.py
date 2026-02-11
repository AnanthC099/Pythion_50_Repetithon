def outer(): 
    N = 100 
    def inner(): 
        # the inner() function wants to modify the outer() function's N 
        # To assign or reassign a value to a variable, it must be used 
        # in the LHS sense 
        # So we write the following statement 
        N = 500 
        # The default LHS variable treatment of Python will look for N 
        # in inner() function's symbol table, it will find N to be absent 
        # and therefore it will create a new symbol table entry for N 
        # and will attach integer object 500 with it. 

        # SO again, we have ended up creating a local version of N instead of 
        # modifying the N in the enclosing scope ! 

        # global N won't help here, because the N that we want to modify is not 
        # present in the global scope ! 

    inner()

outer() 