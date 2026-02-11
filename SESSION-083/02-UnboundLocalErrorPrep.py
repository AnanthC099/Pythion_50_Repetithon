#num = 100 
def test_function(): 
    print('num:', num)
    num = 200 
    print('num:', num)
test_function() 

# RIGHT: LEGB CORRECTLY APPLY 
# num : 100 
# num : 200 

# WRONG

# LAZY EVALUATION 
# GREEDY EVLUATION 