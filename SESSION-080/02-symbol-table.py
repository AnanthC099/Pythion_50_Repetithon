# Module symbol table or global symbol table 

print('globals():', globals())  # This will not be empty 
                                # Lot of variables with __X__ (Ignore them)
                                # Newly defined symbols will be at the end 
print('-----------------------------------------------------------------------') 
gnum = 5000 

print('globals():after gnum = 5000', globals()) # look for the last item in dictionary 
                                                # to get gnum 
print('-----------------------------------------------------------------------')
import math 
import json

print('globals():after import math and import json:', globals()) # look for the last two items in
                                                                 # dictionary to get math and json
                                                                 # entries
print('-----------------------------------------------------------------------')
def test_function(): 
    print("1:initial state of local symbol table:locals():", locals()) # {} 
    b1 = False 
    print("2:local symbol table after b1 = False:", locals()) # {'b1': False}
    n = 300 
    print("3:local symbol table after n = 300:", locals()) # {'b1': False, 'n' : 300}
    f = 3.4 
    print("4:local symbol table after f = 3.4:", locals()) # {'b1':False, 'n':300, 'f':3.4}

test_function() 
print('-----------------------------------------------------------------------')