import sys 

# The built-in package sys of Python programming language 
# defines a variable named 'argv' (stands for argument vector). 

# This variable names a list of string where each string represents 
# an argument on the command-line 

# We can iterate thorugh this this list using indexing or using for loop 

print('ARGUMENTS ON THE COMMAND-LINE IN THE CURRENT INVOCATION:')

print('Printing the entire list of command line arguments:')
print('type(sys.argv):', type(sys.argv)) # Expected output: class list 
print('sys.argv:', sys.argv)

print('Printing using for loop:')
for word in sys.argv: 
    print(word) 

print('Printing using while loop')
i = 0 
while i < len(sys.argv): 
    print('sys.argv[', i, ']:', sys.argv[i])
    i = i + 1


# python mycopy.py abc.txt pqr.txt -> COMMAND LINE 
# mycopy.py -> COMMAND LINE ARGUMENT 
# abc.txt -> COMMAND LINE ARGUMENT 
# pqr.txt -> COMMAND LINE ARGUMENT 