"""
Simplified version of SESSION-068/01-extra-non-keyword-argument.py

ORIGINAL: Long inline comments explaining variadic functions,
verbose commented-out examples.
SIMPLIFIED: Same concept, cleaner demonstration.
"""


def my_variadic_function(*args):
    """Accepts any number of arguments (variadic function)."""
    print(f"Received {len(args)} argument(s): {args}")
    for x in args:
        print(f"  -> {x}")


# Zero parameters
my_variadic_function()

# One parameter
my_variadic_function(10)

# Two parameters
my_variadic_function(10, 20)

# Three parameters
my_variadic_function(10, 20, 30)
