# LAMBDA-IDLE-LOG.py
# Converted from IDLE session log to a runnable Python script
# Demonstrates: lambda expressions, def equivalence, default args, *args, closures

# --- Section 1: Lambda creates a function object, just like def ---
print('--- Lambda vs def: both create function objects ---')

sq_lambda = (lambda n : n ** 2)
print('lambda object:', sq_lambda)

def func(n):
    return n ** 2

print('def object:   ', func)

#---------------------------------------------------

# --- Section 2: Lambda body must be an expression, not a statement ---
print('\n--- Lambda cannot contain statements (like if:) ---')
# The following would be a SyntaxError:
#   result = (lambda n : if n % 2 == 0: print(n, 'is an even number'))(100)
# Use a conditional expression instead:
result = (lambda n : print(n, 'is an even number') if n % 2 == 0 else None)(100)

#-----------------------------------------------------

# --- Section 3: Default parameters work the same way ---
print('\n--- Default parameters: def vs lambda ---')

def myFunc(a, b, c=100):
    print(a, b, c)

myFunc(10, 20)
myFunc(10, 20, c=200)

(lambda a, b, c=100 : print(a, b, c))(10, 20)
(lambda a, b, c=100 : print(a, b, c))(10, 20, c=200)

#-------------------------------------------------------

# --- Section 4: *args (variable-length arguments) ---
print('\n--- *args: def vs lambda ---')

def myFunc(*args):
    print(args)

myFunc()
myFunc(100)
myFunc(100, 200)
myFunc(100, 200, 300)

(lambda *args : print(args))()
(lambda *args : print(args))(100)
(lambda *args : print(args))(100, 200)
(lambda *args : print(args))(100, 200, 300)

#----------------------------------------------------------

# --- Section 5: Lambda with free variables (closure) ---
print('\n--- Lambda with free variables from enclosing scope ---')

a = 1.1
b = 2.2
c = 3.3

# The original IDLE session had a typo: b&y instead of b*y
# (lambda x, y, z : (a*x + b&y + c*z)*3.0)(10, 20, 30)
# -> TypeError: unsupported operand type(s) for &: 'float' and 'float'

# Correct version uses * (multiplication) not & (bitwise AND):
result = (lambda x, y, z : (a*x + b*y + c*z)*3.0)(10, 20, 30)
print('lambda result:', result)

# Verification:
verification = (1.1 * 10 + 2.2 * 20 + 3.3 * 30) * 3.0
print('verification: ', verification)

#---------------------------------------------------------
