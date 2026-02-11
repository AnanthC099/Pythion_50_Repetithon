"""
======================================================================================
    COMPREHENSIVE DOCUMENTATION: def STATEMENT AND ITS FEATURES
======================================================================================

    This file covers:
        PART 1  : def Statement — Basics (SESSION-010, 011, 042)
        PART 2  : Advanced def Statement — Nested def (SESSION-079, 080)
        PART 3  : globals() and locals() — Symbol Tables (SESSION-080)
        PART 4  : Scopes, LEGB Rule, UnboundLocalError, NameError (SESSION-081, 082, 083)
        PART 5  : global Statement and nonlocal Statement (SESSION-084)
        PART 6  : Implicit State Saving, Closures, Function Factory (SESSION-085, 086)
        PART 6A : Function Object Attributes (__name__, __dict__, __annotations__, __code__)
        PART 6B : Local Static-Like Variables in Python (closure & function attribute)
        PART 7  : Parameter Passing — Exhaustive Treatment (SESSION-068, 087, 088)
        PART 8  : Universal Function Wrapper (*args, **kwargs, decorator pattern)

======================================================================================
"""

# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 1 : def STATEMENT — BASICS (SESSION-010, 011, 042)                         ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
GENERAL FORMAT OF def STATEMENT:

    def function_name(formal_parameter_list):
        statement-1
        statement-2
        .
        .
        statement-N

KEY POINTS:
    - def is a keyword and a compound statement
    - function_name follows Python identifier rules
    - formal_parameter_list can be empty or contain one or more parameters
    - The body is indented and forms the function's block
    - return statement is used to send a value back to the caller
"""

# --- 1.1 Basic function definition and calling (SESSION-010) ---
print('=' * 70)
print('PART 1: def STATEMENT — BASICS')
print('=' * 70)

print('\n--- 1.1 Basic function definition and calling ---')

def DisplayBirthdayWishes(personName):
    print('Happy Birthday,')
    print(personName, '!')

# Calling with non-keyword (positional) syntax
DisplayBirthdayWishes('Yogeshwar')
DisplayBirthdayWishes('Ananth')

# Calling with keyword syntax
DisplayBirthdayWishes(personName='Radhika')

# --- 1.2 Function with 0, 1, 2 formal parameters (SESSION-011) ---
print('\n--- 1.2 Function with 0 formal parameters ---')

def TestFunction_0():
    print('  This is a TestFunction() with no parameters')

TestFunction_0()

print('\n--- 1.3 Function with 1 formal parameter ---')

def TestFunction_1(param_1):
    print('  Value of param_1:', param_1)
    print('  Type of param_1:', type(param_1))
    print('  Id of param_1:', id(param_1))

TestFunction_1(1500)
TestFunction_1(1.1)
TestFunction_1('Yogeshwar')

print('\n--- 1.4 Function with 2 formal parameters ---')

def TestFunction_2(x, y):
    print('  Value of x:', x, '| Type:', type(x))
    print('  Value of y:', y, '| Type:', type(y))

TestFunction_2(100, 200)
TestFunction_2(100, 'Hello')
TestFunction_2('Hello', 'World')

# --- 1.5 Type annotations, input validation, exception handling (SESSION-042) ---
print('\n--- 1.5 Type annotations, input validation, exception handling ---')

def linear_search(L, search_data: int) -> bool:
    if type(L) != list:
        raise TypeError('Bad type for L')
    if type(search_data) != int:
        raise TypeError('Bad type for search data')
    for x in L:
        if type(x) != int:
            raise TypeError('Bad type for input elements')
        if x == search_data:
            return True
    return False

result = linear_search([10, 20, 30, 40, 50], 30)
print('  linear_search([10,20,30,40,50], 30):', result)

result = linear_search([10, 20, 30, 40, 50], 99)
print('  linear_search([10,20,30,40,50], 99):', result)


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 2 : ADVANCED def — NESTED def STATEMENT (SESSION-079, 080)                 ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
NESTED def STATEMENT:
    - A function defined inside another function
    - The inner function is a LOCAL variable of the outer function
    - The inner function is created each time the outer function executes
    - The inner function can only be called from within the outer function
      (unless it is returned)
    - Supports 2-level, 3-level, and deeper nesting
"""

print('\n' + '=' * 70)
print('PART 2: NESTED def STATEMENT')
print('=' * 70)

# --- 2.1 Basic nested def — def under def (SESSION-079) ---
print('\n--- 2.1 Basic nested def (def under def) ---')

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

# --- 2.2 Two-level nesting (SESSION-080) ---
print('\n--- 2.2 Two-level nesting ---')

def f1(n):
    print(f'  n:{n}')
    def f2(x, y):
        print(f'  x:{x}, y:{y}')
    z = 100
    print(f'  z:{z}')
    f2(True, False)
f1(500)

# --- 2.3 Three-level nesting (SESSION-080) ---
print('\n--- 2.3 Three-level nesting ---')

def f():
    m = 100
    def g():
        n = 200
        def h():
            k = 300
            print('  h(): k =', k)
        h()
        print('  g(): n =', n)
    g()
    print('  f(): m =', m)
f()


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 3 : globals() AND locals() — SYMBOL TABLES (SESSION-080)                   ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
SYMBOL TABLES IN PYTHON:
    - Every scope has its own symbol table (a dictionary mapping names to objects)
    - globals() returns the global (module) symbol table
    - locals() returns the local symbol table of the current scope
    - At module level, globals() and locals() return the same dictionary
    - Inside a function, locals() returns that function's local symbol table
"""

print('\n' + '=' * 70)
print('PART 3: globals() AND locals() — SYMBOL TABLES')
print('=' * 70)

# --- 3.1 Global symbol table (SESSION-080) ---
print('\n--- 3.1 Global symbol table ---')

gnum = 5000
print('  After gnum = 5000, "gnum" in globals():', 'gnum' in globals())

# --- 3.2 Local symbol table inside a function (SESSION-080) ---
print('\n--- 3.2 Local symbol table inside a function ---')

def test_function_locals():
    print("  1: initial state of locals():", locals())
    b1 = False
    print("  2: after b1 = False:", locals())
    n = 300
    print("  3: after n = 300:", locals())
    f = 3.4
    print("  4: after f = 3.4:", locals())

test_function_locals()

# --- 3.3 One Definition Rule — same name in different scopes (SESSION-082) ---
print('\n--- 3.3 One Definition Rule — same name in different scopes ---')

"""
A variable name can be defined only once in a given scope.
If you change the scope, the same variable name can be recreated independently.
"""

N_global = 100
def f1_odr():
    N_local_f1 = 200
    print('  local symbol table of f1():', locals())
    def f2_odr():
        N_local_f2 = 300
        print('  local symbol table of f2():', locals())
    f2_odr()

f1_odr()
print('  N_global in globals():', 'N_global' in globals())


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 4 : SCOPES, LEGB RULE, UnboundLocalError, NameError (SESSION-081,082,083)  ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
SCOPES IN PYTHON:
    Only 4 entities have their own scope (symbol table):
        1) Module (global scope)
        2) Function (local scope) — created by def statement
        3) Class (class scope) — created by class statement
        4) Object (object namespace)

    Block statements (if, for, while, try-except, with) DO NOT create new scopes.

LHS VARIABLE TREATMENT:
    When a variable name appears on LHS for the first time in a scope,
    Python creates it in that scope's symbol table.

RHS VARIABLE TREATMENT — LEGB SCOPE RULE:
    When a variable name appears on RHS, Python searches in this order:
        L — Local scope
        E — Enclosing scope (for nested functions)
        G — Global scope
        B — Built-in scope
    If not found in any scope, NameError is raised.

7 WAYS A VARIABLE NAME CAN BE USED IN LHS SENSE:
    1) a = 100                    (assignment)
    2) def f(): ...               (function definition)
    3) class T: ...               (class definition)
    4) import Package             (import statement)
    5) with RHS as v: ...         (with-as statement)
    6) except ExceptionName as e: (except-as clause)
    7) for x in L: ...            (for loop variable)
"""

print('\n' + '=' * 70)
print('PART 4: SCOPES, LEGB RULE, UnboundLocalError, NameError')
print('=' * 70)

# --- 4.1 Global and Local Scope demo (SESSION-081) ---
print('\n--- 4.1 Global and local scope demonstration ---')

L_scope = [10, 20, 30, 40, 50]               # global scope
for x_scope in L_scope:                       # global scope
    pass                                       # global scope — x_scope is global

def my_func_scope():                           # global scope
    D = {'a': 100, 'b': 200, 'c': 300}        # local scope wrt my_func_scope()
    for (key, value) in D.items():             # local scope wrt my_func_scope()
        if value > 100:                        # local scope wrt my_func_scope()
            print(f'  {key}: {value}')         # local scope wrt my_func_scope()

my_func_scope()

# --- 4.2 Enclosing scope demonstration (SESSION-081) ---
print('\n--- 4.2 Enclosing scope demonstration ---')

def f1_enc():                                       # global
    L = [10, 20, 30, 40]                            # local wrt f1_enc()
    def f2_enc():                                   # local wrt f1_enc()
        D = {'p': True, 'q': False}                 # local wrt f2_enc(), enclosing with f1_enc()
        def f3_enc():                               # local wrt f2_enc()
            S = {100, 200, 300}                     # local wrt f3_enc()
            for x in S:
                print(f'  f3_enc: {x}^2 = {x**2}')
        f3_enc()
        for (key, val) in D.items():
            print(f'  f2_enc: {key} = {val}')
    f2_enc()
    print(f'  f1_enc: L = {L}')

f1_enc()

# --- 4.3 LEGB Rule demonstrations (SESSION-082) ---
print('\n--- 4.3 LEGB Rule demonstrations ---')

# Snippet 1: Local scope shadows global
print('\n  Snippet 1: Local scope shadows global')
N_legb = 100
def f_legb_1():
    N_legb = 200
    print('  f():N:', N_legb)       # prints 200 (local shadows global)
print('  global:N:', N_legb)        # prints 100 (global)
f_legb_1()

# Snippet 2: No local N, LEGB finds it in global
print('\n  Snippet 2: No local N, LEGB finds it in global')
N_legb2 = 100
def f_legb_2():
    print('  f():N:', N_legb2)      # prints 100 (found in global scope)
f_legb_2()

# Snippet 3: Enclosing scope lookup
print('\n  Snippet 3: Enclosing scope lookup')
N_legb3 = 100
def f1_legb_3():
    N_legb3 = 200
    def f2_legb_3():
        print('  f2():N:', N_legb3) # prints 200 (found in enclosing f1 scope)
    f2_legb_3()
f1_legb_3()

# LEGB with 4-level nesting (SESSION-083)
print('\n  LEGB with 4-level nesting (SESSION-083)')
N_deep = 10
def f1_deep():
    N_deep = 100
    def f2_deep():
        N_deep = 1000
        def f3_deep():
            N_deep = 10000
            print('  f3:N:', N_deep)    # prints 10000 (local)
        f3_deep()
    f2_deep()
f1_deep()

# --- 4.4 UnboundLocalError (SESSION-082, 083) ---
print('\n--- 4.4 UnboundLocalError ---')

"""
UnboundLocalError occurs when:
    - A variable is used on LHS ANYWHERE in a function
    - Python marks it as LOCAL for the ENTIRE function at compile time
    - If it is accessed on RHS BEFORE the LHS assignment, UnboundLocalError is raised

KEY INSIGHT: Python determines scope at COMPILE TIME, not at RUNTIME.
"""

# Case 1: print(n) before n = 200
print('\n  Case 1: print(n) before n = 200')
N_uble1 = 100
def f_uble_1():
    try:
        print(N_uble1)      # UnboundLocalError: n is local due to line below
        N_uble1 = 200
    except UnboundLocalError as e:
        print(f'  UnboundLocalError: {e}')
f_uble_1()

# Case 2: n = n + 1 (extreme case — hard to spot)
print('\n  Case 2: n = n + 1 (hard to spot)')
N_uble2 = 100
def f_uble_2():
    try:
        N_uble2 = N_uble2 + 1   # UnboundLocalError: n used on LHS makes it local
    except UnboundLocalError as e:
        print(f'  UnboundLocalError: {e}')
f_uble_2()

# --- 4.5 NameError — Free Variable Version (SESSION-082, 084) ---
print('\n--- 4.5 NameError — Free Variable Version ---')

"""
A free variable in a nested function references a variable from the enclosing scope.
The variable must be BOUND (have a value) at the time the inner function EXECUTES.
Scope determination happens at compile time, but value lookup happens at runtime.
"""

# No Error: n defined before inner is called
print('\n  Case 1: No error — n defined before g() is called')
def f_ne_1():
    n_ne = 100
    def g_ne():
        print('  g():n:', n_ne)
    g_ne()
f_ne_1()

# No Error: n defined after g() is defined but before g() is called
print('\n  Case 2: No error — n defined after g() definition but before g() call')
def f_ne_2():
    def g_ne():
        print('  g():n:', n_ne)
    n_ne = 100
    g_ne()
f_ne_2()

# Error: g() called before n is assigned
print('\n  Case 3: NameError — g() called before n = 100 executes')
def f_ne_3():
    def g_ne():
        try:
            print(n_ne)     # NameError: free variable 'n_ne' not yet bound
        except NameError as e:
            print(f'  NameError: {e}')
    g_ne()
    n_ne = 100
f_ne_3()

# Error: n deleted before g() is called
print('\n  Case 4: NameError — n deleted with del before g() is called')
def f_ne_4():
    n_ne = 100
    def g_ne():
        try:
            print(n_ne)     # NameError: free variable deleted
        except NameError as e:
            print(f'  NameError: {e}')
    del n_ne
    g_ne()
f_ne_4()


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 5 : global STATEMENT AND nonlocal STATEMENT (SESSION-084)                  ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
global STATEMENT:
    Syntax:
        global variable_name
        global v1, v2, ..., vn    (comma-separated list)

    Constraints:
        - Must be written inside a function definition (body of def statement)

    Behaviour:
        - All references (RHS or LHS) to that variable in that function
          are bound to the global symbol table
        - Overrides usual LHS treatment and RHS treatment (LEGB rule)

nonlocal STATEMENT:
    Syntax:
        nonlocal variable_name
        nonlocal v1, v2, ..., vn  (comma-separated list)

    Constraints:
        - Must be used inside a nested function
        - The variable must exist in an enclosing scope (not global)

    Behaviour:
        - Binds the variable to the nearest enclosing scope's symbol table
        - Allows modification of enclosing scope variables from inner function
"""

print('\n' + '=' * 70)
print('PART 5: global STATEMENT AND nonlocal STATEMENT')
print('=' * 70)

# --- 5.1 global statement — Scenario 1: Access hidden global (SESSION-084) ---
print('\n--- 5.1 global statement — Access hidden global variable ---')

# BEFORE: global N hidden by enclosing N
print('  BEFORE (global N hidden by enclosing N):')
N_gs1 = 100
def outer_gs1_before():
    N_gs1 = 200
    def inner_gs1_before():
        print('  inner():N:', N_gs1)  # prints 200 (enclosing, NOT global)
    inner_gs1_before()
outer_gs1_before()

# AFTER: using global statement to access global N
print('  AFTER (using global statement):')
N_gs1 = 100
def outer_gs1_after():
    N_gs1 = 200
    def inner_gs1_after():
        global N_gs1
        print('  inner():N:', N_gs1)   # prints 100 (global N)
        N_gs1 = 500
    inner_gs1_after()
outer_gs1_after()
print('  global N after inner() modified it:', N_gs1)

# --- 5.2 global statement — Scenario 2-A: Modify global variable (SESSION-084) ---
print('\n--- 5.2 global statement — Modify global from inside function ---')

# BEFORE: local N created instead of modifying global N
print('  BEFORE (local N created, global N untouched):')
N_gs2a = 100
def f_gs2a_before():
    N_gs2a = 500        # Creates local, does NOT modify global
f_gs2a_before()
print('  global N after f():', N_gs2a)      # still 100

# AFTER: using global statement
print('  AFTER (using global statement):')
N_gs2a = 100
def f_gs2a_after():
    global N_gs2a
    N_gs2a = 500
print('  global N before f():', N_gs2a)
f_gs2a_after()
print('  global N after f():', N_gs2a)      # now 500

# --- 5.3 global statement — Scenario 2-B: Increment global (SESSION-084) ---
print('\n--- 5.3 global statement — Increment global from inside function ---')

N_gs2b = 100
def f_gs2b():
    global N_gs2b
    N_gs2b = N_gs2b + 1
print('  global N before f():', N_gs2b)
f_gs2b()
print('  global N after f():', N_gs2b)      # now 101

# --- 5.4 nonlocal statement — Prep (SESSION-084) ---
print('\n--- 5.4 nonlocal statement — Problem demonstration ---')

"""
Problem: inner() wants to modify outer()'s N.
  - N = 500 in inner() creates a LOCAL version (default LHS treatment)
  - global N won't help because N we want is NOT in global scope
  - Solution: nonlocal N
"""

def outer_nl_problem():
    N = 100
    def inner_nl_problem():
        N = 500         # Creates local N, does NOT modify outer's N
    print('  outer N before inner():', N)
    inner_nl_problem()
    print('  outer N after inner():', N)     # still 100

outer_nl_problem()

# --- 5.5 nonlocal statement — Solution (SESSION-084) ---
print('\n--- 5.5 nonlocal statement — Solution ---')

def outer_nl():
    N = 500
    def inner_nl():
        nonlocal N
        N = 1000
    print('  outer():N before call to inner():', N)
    inner_nl()
    print('  outer():N after call to inner():', N)     # now 1000
outer_nl()

# --- 5.6 nonlocal statement — Deep nesting (SESSION-084) ---
print('\n--- 5.6 nonlocal with deep nesting ---')

def f1_nl_deep():
    N = 100
    def f2_nl_deep():
        def f3_nl_deep():
            def f4_nl_deep():
                nonlocal N
                N = 200
            f4_nl_deep()
        f3_nl_deep()
    print('  f1():Before call to f2():N:', N)
    f2_nl_deep()
    print('  f1():After call to f2():N:', N)     # now 200
f1_nl_deep()


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 6 : IMPLICIT STATE SAVING, CLOSURES, FUNCTION FACTORY (SESSION-085, 086)   ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
IMPLICIT STATE SAVING (CLOSURES):
    - When outer function returns an inner function (as a data object)
    - The inner function retains access to the outer function's variables
      even after the outer function has finished execution
    - This is because the inner function's free variables are saved in a closure

FUNCTION FACTORY DESIGN PATTERN:
    - A function that creates and returns other functions
    - Each returned function retains its own state via closure
    - Higher-order function: a function that returns a function
"""

print('\n' + '=' * 70)
print('PART 6: IMPLICIT STATE SAVING, CLOSURES, FUNCTION FACTORY')
print('=' * 70)

# --- 6.1 Returning function as data object (SESSION-085) ---
print('\n--- 6.1 Returning function as data object ---')

def outer_ret():
    def inner_ret():
        print('  inner():Function entered')
        print('  inner():Function leaving')
    print('  outer():type(inner):', type(inner_ret))
    print('  outer():id(inner):', id(inner_ret))
    return inner_ret

X_ret = outer_ret()
print('  global:type(X):', type(X_ret))
print('  global:id(X):', id(X_ret))
print('  Putting call operator on global variable X:')
X_ret()

# --- 6.2 Implicit state saving — Closure (SESSION-085) ---
print('\n--- 6.2 Implicit state saving — Closure ---')

def outer_iss():
    num = 500
    def inner_iss():
        print('  inner():num:', num)      # num is a free variable — saved in closure
    print('  outer():type(inner):', type(inner_iss))
    return inner_iss

X_iss = outer_iss()
print('  Calling X() — outer() has finished, but num is still accessible:')
X_iss()                                     # prints 500!

# --- 6.3 Closure characterization (SESSION-086) ---
print('\n--- 6.3 Closure — Pattern comparison ---')

# Pattern 1: Inner function called inside outer (normal nesting)
print('  Pattern 1: inner() called inside outer()')
def outer_p1():
    N_p1 = 100
    def inner_p1():
        print('  inner():N:', N_p1)
    inner_p1()
outer_p1()

# Pattern 2: Inner function returned and called outside (closure)
print('  Pattern 2: inner() returned and called outside (CLOSURE)')
def outer_p2():
    N_p2 = 100
    def inner_p2():
        print('  inner():N:', N_p2)
    return inner_p2
X_p2 = outer_p2()
X_p2()

# --- 6.4 Function Factory — PowerFunctionFactory (SESSION-086) ---
print('\n--- 6.4 Function Factory — PowerFunctionFactory ---')

def PowerFunctionFactory(N: int):
    def InnerFunction(x: float):
        return x ** N
    return InnerFunction

mySquareFunction = PowerFunctionFactory(2)
myCubeFunction = PowerFunctionFactory(3)
myRaisedToSevenFunction = PowerFunctionFactory(7)

result = mySquareFunction(2)
print('  mySquareFunction(2):', result)              # 4

result = myCubeFunction(2)
print('  myCubeFunction(2):', result)                # 8

result = myRaisedToSevenFunction(2)
print('  myRaisedToSevenFunction(2):', result)       # 128

# --- 6.5 Implicit state vs Explicit state (CLASS) comparison (SESSION-086) ---
print('\n--- 6.5 Implicit state (closure) vs Explicit state (class) ---')

# Using closure (implicit state saving with nonlocal)
print('  Using CLOSURE (nested def + nonlocal):')
def test_closure(init_n):
    N = init_n
    def getn():
        nonlocal N
        return N
    def setn(newN):
        nonlocal N
        N = newN
    return (getn, setn)

getn, setn = test_closure(100)
print('  getn():', getn())       # 100
setn(200)
print('  getn():', getn())       # 200
setn(500)
print('  getn():', getn())       # 500

# Equivalent class (explicit state)
print('\n  Equivalent CLASS (explicit state):')

class TestExplicit:
    def __init__(self, init_n):
        self.N = init_n
    def getn(self):
        return self.N
    def setn(self, newN):
        self.N = newN

t = TestExplicit(100)
print('  t.getn():', t.getn())   # 100
t.setn(200)
print('  t.getn():', t.getn())   # 200
t.setn(500)
print('  t.getn():', t.getn())   # 500


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 6A : FUNCTION OBJECT ATTRIBUTES (ADVANCED def FEATURE)                     ║
# ║  function.__name__, __dict__, __annotations__, __code__                           ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
FUNCTION OBJECT ATTRIBUTES:
    Every function in Python is an object of type <class 'function'>.
    Function objects have several built-in attributes that provide
    introspection into the function's metadata:

    function.__name__        : The name of the function as a string
    function.__dict__        : The function's namespace (custom attributes)
    function.__annotations__ : Dictionary of parameter and return type annotations
    function.__code__        : The compiled bytecode object of the function

    These attributes allow you to inspect functions at runtime —
    what they are called, what types they expect, and even their bytecode details.
"""

print('\n' + '=' * 70)
print('PART 6A: FUNCTION OBJECT ATTRIBUTES')
print('  function.__name__, __dict__, __annotations__, __code__')
print('=' * 70)

# --- 6A.1 function.__name__ ---
print('\n--- 6A.1 function.__name__ ---')

def greet(name: str) -> str:
    return f'Hello, {name}!'

print('  greet.__name__:', greet.__name__)           # 'greet'

def outer_name_demo():
    def inner_name_demo():
        pass
    print('  inner.__name__:', inner_name_demo.__name__)  # 'inner_name_demo'
    return inner_name_demo

X_name = outer_name_demo()
print('  X.__name__ (returned inner function):', X_name.__name__)  # still 'inner_name_demo'

# --- 6A.2 function.__annotations__ ---
print('\n--- 6A.2 function.__annotations__ ---')

def compute(a: int, b: float, c: str = 'default') -> bool:
    return True

print('  compute.__annotations__:', compute.__annotations__)
# {'a': <class 'int'>, 'b': <class 'float'>, 'c': <class 'str'>, 'return': <class 'bool'>}

def linear_search_annotated(L: list, search_data: int) -> bool:
    for x in L:
        if x == search_data:
            return True
    return False

print('  linear_search_annotated.__annotations__:', linear_search_annotated.__annotations__)

def no_annotations(a, b, c):
    pass

print('  no_annotations.__annotations__:', no_annotations.__annotations__)  # {}

# --- 6A.3 function.__dict__ ---
print('\n--- 6A.3 function.__dict__ (custom attributes on function objects) ---')

def my_func():
    pass

print('  my_func.__dict__ (initial):', my_func.__dict__)   # {}

# You can attach custom attributes to function objects
my_func.version = '1.0'
my_func.author = 'Yogeshwar'

print('  my_func.__dict__ (after adding attributes):', my_func.__dict__)
# {'version': '1.0', 'author': 'Yogeshwar'}

print('  my_func.version:', my_func.version)
print('  my_func.author:', my_func.author)

# --- 6A.4 function.__code__ ---
print('\n--- 6A.4 function.__code__ (bytecode object) ---')

def sample_func(x, y, z):
    result = x + y + z
    return result

code_obj = sample_func.__code__
print('  sample_func.__code__:', code_obj)
print('  co_varnames (local variable names):', code_obj.co_varnames)
# ('x', 'y', 'z', 'result')
print('  co_argcount (number of positional args):', code_obj.co_argcount)
# 3
print('  co_name (function name from bytecode):', code_obj.co_name)
# 'sample_func'

# Demonstrating with nested function
def outer_code():
    N = 100
    def inner_code(a, b):
        return a + b + N
    return inner_code

inner_ref = outer_code()
print('\n  inner function __code__:')
print('  co_varnames:', inner_ref.__code__.co_varnames)
print('  co_argcount:', inner_ref.__code__.co_argcount)
print('  co_freevars (free variables from enclosing scope):', inner_ref.__code__.co_freevars)
# ('N',)

# --- 6A.5 Summary: All key function attributes at a glance ---
print('\n--- 6A.5 All key function attributes at a glance ---')

def demo_all(a: int, b: float = 2.5) -> str:
    """A demo function showing all attributes."""
    result = str(a) + str(b)
    return result

print(f'  __name__        : {demo_all.__name__}')
print(f'  __annotations__ : {demo_all.__annotations__}')
print(f'  __dict__        : {demo_all.__dict__}')
print(f'  __doc__         : {demo_all.__doc__}')
print(f'  __defaults__    : {demo_all.__defaults__}')
print(f'  __code__.co_varnames  : {demo_all.__code__.co_varnames}')
print(f'  __code__.co_argcount  : {demo_all.__code__.co_argcount}')


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 6B : LOCAL STATIC-LIKE VARIABLES IN PYTHON (ADVANCED def FEATURE)          ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
LOCAL STATIC-LIKE VARIABLES IN PYTHON:
    In C/C++, a static local variable retains its value between function calls.
    Python does NOT have a 'static' keyword, but closures (implicit state saving)
    provide equivalent functionality.

    When a nested function (inner) retains access to a variable from its
    enclosing scope (outer) even after the outer function has returned,
    the enclosing variable behaves like a "local static variable" — it persists
    across multiple calls to the inner function.

    Two techniques:
    1) Closure with nonlocal — inner function reads and modifies enclosing variable
    2) Function attribute — store state directly on the function object via __dict__
"""

print('\n' + '=' * 70)
print('PART 6B: LOCAL STATIC-LIKE VARIABLES IN PYTHON')
print('=' * 70)

# --- 6B.1 Static-like variable using closure (nonlocal) ---
print('\n--- 6B.1 Static-like variable using closure (nonlocal) ---')

def make_counter():
    count = 0               # This acts as a "static local variable"
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = make_counter()
print('  Call 1:', my_counter())    # 1
print('  Call 2:', my_counter())    # 2
print('  Call 3:', my_counter())    # 3
print('  Call 4:', my_counter())    # 4
# count persists across calls — behaves like C static local variable!

# Each call to make_counter() creates an independent counter
another_counter = make_counter()
print('  another_counter Call 1:', another_counter())   # 1 (independent!)
print('  my_counter Call 5:', my_counter())             # 5 (continues from 4)

# --- 6B.2 Static-like variable using function attribute ---
print('\n--- 6B.2 Static-like variable using function __dict__ ---')

def counter_with_attr():
    counter_with_attr.count += 1
    return counter_with_attr.count

counter_with_attr.count = 0     # Initialize via function's __dict__

print('  Call 1:', counter_with_attr())    # 1
print('  Call 2:', counter_with_attr())    # 2
print('  Call 3:', counter_with_attr())    # 3
print('  __dict__:', counter_with_attr.__dict__)   # {'count': 3}

# --- 6B.3 Accumulator — practical use of static-like variable ---
print('\n--- 6B.3 Accumulator — practical use of static-like variable ---')

def make_accumulator(initial_value=0):
    total = initial_value
    def accumulate(amount):
        nonlocal total
        total += amount
        return total
    return accumulate

acc = make_accumulator(0)
print('  acc(10):', acc(10))    # 10
print('  acc(20):', acc(20))    # 30
print('  acc(5):', acc(5))      # 35
print('  acc(15):', acc(15))    # 50
# total persists across calls like a static variable!


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 7 : PARAMETER PASSING — EXHAUSTIVE TREATMENT (SESSION-068, 087, 088)       ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
SIX TYPES OF FORMAL PARAMETERS:
    1) Positional argument
    2) Keyword argument (calling with keyword syntax)
    3) Extra non-keyword argument (*args)
    4) Default argument
    5) Keyword-only argument (after *args)
    6) Extra keyword argument (**kwargs)

TWO WAYS OF WRITING ACTUAL PARAMETERS:
    1) Non-keyword syntax:  f(10, 20, 30)
    2) Keyword syntax:      f(a=10, b=20, c=30)

GOLDEN RULE:
    Once you start using keyword syntax, you CANNOT fall back to non-keyword syntax.

INSIGHT 1: Positional params can be called using keyword syntax.
INSIGHT 2: Default params can be called using non-keyword syntax.

NON-DEFAULT AFTER DEFAULT RULE:
    You cannot have a non-default parameter after a default parameter
    UNLESS *args separates them (keyword-only arguments).
"""

print('\n' + '=' * 70)
print('PART 7: PARAMETER PASSING — EXHAUSTIVE TREATMENT')
print('=' * 70)

# --- 7.1 Positional argument (SESSION-087) ---
print('\n--- 7.1 Positional argument ---')

def positional_demo(a, b, c):
    print(f'  a={a}, b={b}, c={c}')

positional_demo(10, 20, 30)

def bool_demo(a, b, c, d):
    print(f'  a={a}, b={b}, c={c}, d={d}')

bool_demo(False, True, False, True)

# --- 7.2 Keyword argument — calling with keyword syntax (SESSION-087) ---
print('\n--- 7.2 Keyword argument (calling with keyword syntax) ---')

positional_demo(a=10, b=20, c=30)
positional_demo(c=30, a=10, b=20)   # order doesn't matter with keyword syntax

# --- 7.3 Extra non-keyword argument *args (SESSION-068, 087, 088) ---
print('\n--- 7.3 Extra non-keyword argument (*args) ---')

# Variadic function concept (SESSION-068)
print('  Variadic function — accepts different number of parameters per call:')

def myVariadicFunction(*myParameter):
    print('  Entered myVariadicFunction')
    print('  myParameter:', myParameter)
    print('  type:', type(myParameter))
    for x in myParameter:
        print('   ', x)

myVariadicFunction()
myVariadicFunction(10)
myVariadicFunction(10, 20)
myVariadicFunction(10, 20, 30)

# *args in isolation (SESSION-088)
print('\n  *args in isolation:')

def testFunction_args_only(*args):
    print('  args:', args, 'type:', type(args))

testFunction_args_only(10, 20, 30, 40)
testFunction_args_only()

# *args with positional params (SESSION-087, 088)
print('\n  *args with positional params:')

def extra_nonkw_demo(a, b, *args):
    print(f'  a={a}, b={b}, args={args}')

extra_nonkw_demo(1, 2)
extra_nonkw_demo(1, 2, 3, 4, 5)

# Positional params before *args (SESSION-088)
print('\n  Positional params before *args:')

def testFunction_positional(a, b, c, *args):
    print(f'  a={a}, b={b}, c={c}')
    print(f'  args={args}')

testFunction_positional(10, 20, 30)
testFunction_positional(10, 20, 30, 40)
testFunction_positional(10, 20, 30, 40, [100, 200, 300])

# --- 7.4 Default argument (SESSION-087, 088) ---
print('\n--- 7.4 Default argument ---')

def default_demo(a, b, c=100):
    print(f'  a={a}, b={b}, c={c}')

default_demo(1, 2)          # c takes default value 100
default_demo(1, 2, 3)       # c overridden to 3

# All defaults (SESSION-088)
print('\n  All defaults:')

def testFunction_default(a=10, b=20, c=30):
    print(f'  a={a}, b={b}, c={c}')

testFunction_default()
testFunction_default(a=100)
testFunction_default(100)
testFunction_default(10, 20, 300)
testFunction_default(c=300)

# --- 7.5 Keyword-only argument — after *args (SESSION-087, 088) ---
print('\n--- 7.5 Keyword-only argument (after *args) ---')

def kwonly_demo(a, b, *args, mode):
    print(f'  a={a}, b={b}, args={args}, mode={mode}')

kwonly_demo(1, 2, 3, 4, mode="fast")

# Keyword-only with positional and *args (SESSION-088)
print('\n  Keyword-only with positional and *args:')

def testFunction_kwonly(a, b, c, *args, p, q):
    print(f'  a={a}, b={b}, c={c}')
    print(f'  args={args}')
    print(f'  p={p}, q={q}')

testFunction_kwonly(10, 20, 30, 40, 50, 60, 70, p=80, q=90)

# --- 7.6 Extra keyword argument **kwargs (SESSION-087, 088) ---
print('\n--- 7.6 Extra keyword argument (**kwargs) ---')

def extra_kw_demo(**kwargs):
    print(f'  kwargs={kwargs}')

extra_kw_demo(x=10, y=20, z=30)
extra_kw_demo()

# **kwargs in isolation (SESSION-088)
print('\n  **kwargs in isolation:')

def testFunction_kwargs_only(**kwargs):
    print('  kwargs:', kwargs)

testFunction_kwargs_only()
testFunction_kwargs_only(a=10, b=20, c=30)

# --- 7.7 The Golden Rule (SESSION-087) ---
print('\n--- 7.7 The Golden Rule ---')
print('  Once you start using keyword syntax, you CANNOT fall back to non-keyword.')

print('\n  Valid calls:')
positional_demo(10, 20, 30)           # all non-keyword
positional_demo(10, 20, c=30)         # switch to keyword at c — OK
positional_demo(10, b=20, c=30)       # switch to keyword at b — OK
positional_demo(a=10, b=20, c=30)     # all keyword — OK

print('\n  Valid — non-keyword + reordered keyword:')
bool_demo(10, d=40, b=20, c=30)       # keyword args can appear in any order

print('\n  Invalid (would raise SyntaxError):')
print('  positional_demo(a=10, 20, 30)')
print('  # SyntaxError: positional argument follows keyword argument')

# --- 7.8 INSIGHT 1: Positional params can be called using keyword syntax (SESSION-087) ---
print('\n--- 7.8 INSIGHT 1: Positional params can be called using keyword syntax ---')

def insight1_demo(x, y, z):
    print(f'  x={x}, y={y}, z={z}')

print('  Non-keyword (positional) call:')
insight1_demo(1, 2, 3)

print('  Keyword call (same function, same result, different order):')
insight1_demo(z=3, x=1, y=2)

# --- 7.9 INSIGHT 2: Default params can be called using non-keyword syntax (SESSION-087) ---
print('\n--- 7.9 INSIGHT 2: Default params can be called using non-keyword syntax ---')

def insight2_demo(a, b=20, c=30):
    print(f'  a={a}, b={b}, c={c}')

print('  Using defaults (omit b and c):')
insight2_demo(1)

print('  Override defaults with non-keyword syntax:')
insight2_demo(1, 200, 300)

print('  Override defaults with keyword syntax:')
insight2_demo(1, c=300)

# --- 7.10 MasterFunction — All parameter types combined (SESSION-088) ---
print('\n--- 7.10 MasterFunction — All parameter types combined ---')

def MasterFunction(a, b, c, *args, x=1.1, y=2.2, p, q, **kwargs):
    print("  Positional arguments")
    print(f"    a:{a}, b:{b}, c:{c}")
    print("  Extra non-keyword arguments")
    for i in range(len(args)):
        print(f"    args[{i}]:{args[i]}")
    print("  Default arguments")
    print(f"    x:{x}, y:{y}")
    print("  Keyword only arguments")
    print(f"    p:{p}, q:{q}")
    print("  Extra-keyword arguments")
    for key, val in kwargs.items():
        print(f"    {key}: {val}")

MasterFunction(10, 20, 30, 40, 50, 60, 70, y=20.25, p=False, q=True, u=False, w=True, v=False)

# --- 7.11 Non-Default-After-Default Rule (SESSION-088) ---
print('\n--- 7.11 Non-Default-After-Default Rule ---')

"""
You CANNOT write a non-default parameter after a default parameter:
    def f(a, b, c, x=1.1, y=2.2, p, q):   # SyntaxError!
    # SyntaxError: parameter without a default follows parameter with a default

Workaround 1: Use *args to introduce keyword-only arguments
    def f(a, b, c, *args, x=1.1, y=2.2, p, q):   # OK! p, q are keyword-only

Workaround 2: Use **kwargs
    def f(a, b, c, x=1.1, y=2.2, **kwargs):       # OK! extra keywords in kwargs
"""

def testFunction_no_args(a, b, c, x=1.1, y=2.2):
    print(f'  a={a}, b={b}, c={c}')
    print(f'  x={x}, y={y}')

testFunction_no_args(10, 20, 30, y=20.25)
testFunction_no_args(10, b=20, c=30, y=20.25)

print('\n  Workaround using **kwargs:')

def testFunction_workaround(a, b, c, x=1.1, y=2.2, **kwargs):
    print(f'  a={a}, b={b}, c={c}')
    print(f'  x={x}, y={y}')
    print(f'  kwargs={kwargs}')

testFunction_workaround(10, 20, 30, y=20.25)


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  PART 8 : UNIVERSAL FUNCTION WRAPPER (ADVANCED def FEATURE)                      ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

"""
UNIVERSAL FUNCTION WRAPPER:
    A function that can wrap ANY other function regardless of its parameter list.
    Uses *args and **kwargs to accept and forward all arguments.

    The universal formal parameter list:  def wrapper(*args, **kwargs)
    This can accept ANY combination of positional and keyword arguments.

    Practical applications:
    - Logging / tracing function calls
    - Timing function execution
    - Decorator pattern (decorator is built on top of universal wrapper)
"""

print('\n' + '=' * 70)
print('PART 8: UNIVERSAL FUNCTION WRAPPER')
print('=' * 70)

# --- 8.1 Universal formal parameter list ---
print('\n--- 8.1 Universal formal parameter list ---')

def universal_accept(*args, **kwargs):
    """This function can accept ANY call signature."""
    print('  args:', args)
    print('  kwargs:', kwargs)

print('  Call with positional only:')
universal_accept(10, 20, 30)

print('  Call with keyword only:')
universal_accept(a=10, b=20, c=30)

print('  Call with mixed:')
universal_accept(10, 20, c=30, d=40)

print('  Call with no arguments:')
universal_accept()

# --- 8.2 Universal function wrapper pattern ---
print('\n--- 8.2 Universal function wrapper pattern ---')

def universal_wrapper(func):
    """Wraps any function — forwards all arguments, returns result."""
    def replacement_function(*args, **kwargs):
        print(f'  [WRAPPER] Calling {func.__name__}')
        print(f'  [WRAPPER] args: {args}')
        print(f'  [WRAPPER] kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'  [WRAPPER] {func.__name__} returned: {result}')
        return result
    return replacement_function

# Apply wrapper to different functions with different signatures

def add(a, b):
    return a + b

def greet_person(name, greeting='Hello'):
    return f'{greeting}, {name}!'

def compute_power(base, *exponents):
    results = []
    for exp in exponents:
        results.append(base ** exp)
    return results

wrapped_add = universal_wrapper(add)
wrapped_greet = universal_wrapper(greet_person)
wrapped_power = universal_wrapper(compute_power)

print('\n  Wrapped add(10, 20):')
wrapped_add(10, 20)

print('\n  Wrapped greet("Ananth", greeting="Namaste"):')
wrapped_greet("Ananth", greeting="Namaste")

print('\n  Wrapped compute_power(2, 1, 2, 3, 4, 5):')
wrapped_power(2, 1, 2, 3, 4, 5)

# --- 8.3 Logger — Real-world universal wrapper (from OPEN_FOR_ALL_WEEK) ---
print('\n--- 8.3 Logger — Real-world universal wrapper ---')

"""
Real-world example from OPEN_FOR_ALL_WEEK/DEMONSTRATION_CODE/logger.py:

    def logger(decorated_function_object):
        def replacement_function(*args, **kwargs):
            # Log function name using decorated_function_object.__name__
            # Log all non-keyword arguments from args
            # Log all keyword arguments from kwargs
            ret = decorated_function_object(*args, **kwargs)
            # Log return value
            return ret
        return replacement_function

Usage with @ decorator syntax:
    @logger
    def compute1(a, b, c):
        return (a - b) * (b + c) + (c - a)

    ret = compute1(10, b=20, c=30)

The logger wraps ANY function regardless of its parameter list
by using the universal wrapper pattern: *args, **kwargs
"""

# Simplified logger demonstration (without file I/O)
def simple_logger(func):
    def replacement(*args, **kwargs):
        print(f'  [LOG] Called: {func.__name__}')
        print(f'  [LOG] Non-keyword args: {args}')
        print(f'  [LOG] Keyword args: {kwargs}')
        ret = func(*args, **kwargs)
        print(f'  [LOG] Return value: {ret}, Type: {type(ret)}')
        return ret
    return replacement

@simple_logger
def compute1(a, b, c):
    rs1 = a - b
    rs2 = b + c
    rs3 = c - a
    return (rs1 * rs2) + rs3

@simple_logger
def compute2(x, y):
    return x**2 - y**2

print('\n  compute1(10, b=20, c=30):')
ret = compute1(10, b=20, c=30)

print('\n  compute2(3, y=1):')
ret = compute2(3, y=1)

# --- 8.4 Timing wrapper — Another practical universal wrapper ---
print('\n--- 8.4 Timing wrapper — Another practical universal wrapper ---')

import time

def timing_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'  [TIMER] {func.__name__} took {end - start:.6f} seconds')
        return result
    return wrapper

@timing_wrapper
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = slow_sum(100000)
print(f'  Result: {result}')


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║  SUMMARY: SESSION MAP                                                            ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

print('\n' + '=' * 70)
print('SESSION MAP — def STATEMENT AND ITS FEATURES')
print('=' * 70)

print("""
  BASIC def STATEMENT:
    SESSION-010 : Introduction to def statement (basic definition & calling)
    SESSION-011 : Function details (0, 1, 2 params; type(), id())
    SESSION-042 : def statement repeatithon (annotations, validation, exceptions)

  ADVANCED def STATEMENT — NESTED def:
    SESSION-079 : Nested def statement (def under def, control flow, memory)
    SESSION-080 : Nested def practice (2-level, 3-level nesting, symbol tables)

  GLOBALS AND LOCALS:
    SESSION-080 : globals(), locals() built-in functions
    SESSION-082 : Global and local symbol tables, One Definition Rule

  SCOPES, LEGB, ERRORS:
    SESSION-081 : Scope theory (module, function, class scope; block != scope)
    SESSION-082 : LHS treatment, LEGB rule, UnboundLocalError, NameError
    SESSION-083 : LEGB demo continued, UnboundLocalError preparation

  global AND nonlocal STATEMENTS:
    SESSION-084 : global statement, nonlocal statement (syntax & solutions)

  CLOSURES AND FUNCTION FACTORY:
    SESSION-085 : Returning functions, implicit state saving (closures)
    SESSION-086 : Function factory, higher-order functions, closure vs class

  FUNCTION OBJECT ATTRIBUTES (ADVANCED def FEATURE):
    function.__name__        : Name of the function as a string
    function.__annotations__ : Dictionary of type annotations
    function.__dict__        : Custom attributes namespace
    function.__code__        : Compiled bytecode (co_varnames, co_argcount, co_freevars)

  LOCAL STATIC-LIKE VARIABLES (ADVANCED def FEATURE):
    Technique 1 : Closure with nonlocal (counter, accumulator patterns)
    Technique 2 : Function attribute via __dict__

  PARAMETER PASSING:
    SESSION-068 : Extra non-keyword arguments (*args), variadic functions
    SESSION-087 : Parameter passing intro (6 types, Golden Rule, Insights)
    SESSION-088 : Parameter passing advanced (MasterFunction, all types combined)

  UNIVERSAL FUNCTION WRAPPER (ADVANCED def FEATURE):
    Universal formal parameter list : def wrapper(*args, **kwargs)
    Universal wrapper pattern       : Wrap any function, forward all arguments
    Logger / Decorator              : Real-world application (OPEN_FOR_ALL_WEEK)
    Timing wrapper                  : Practical example of decorator pattern
""")

print('=' * 70)
print('END OF DOCUMENTATION')
print('=' * 70)
