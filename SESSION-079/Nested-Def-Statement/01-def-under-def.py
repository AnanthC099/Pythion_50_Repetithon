print('start of program')

def outer_function(): 
    print('\t----outer function entered----')
    print('\t----defining inner function----')
    def inner_function(): 
        print('\t\t----inner function entered----')
        print('\t\t----inner function leaving----')
    print('\t----done defining the inner function----')
    print('\t----calling the inner function----')
    inner_function() 
    print('\t----returned from inner function----')
    print('\t----returning from outer function----')

print('done defining outer function')
print('calling outer function')
outer_function() 
print('returned from outer function')
print('end of program')
