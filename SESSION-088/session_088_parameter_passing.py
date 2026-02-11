"""
Session 088: Python Parameter Passing
Topics covered:
  1. Extra non-keyword arguments (*args) - isolation and with positional params
  2. Keyword-only arguments (after *args)
  3. Default arguments
  4. Extra keyword arguments (**kwargs)
  5. MasterFunction integrating all parameter types
  6. Non-default after default parameter rule
"""

print("=" * 60)
print("SESSION 088: PARAMETER PASSING")
print("=" * 60)

# ── 1. Extra non-keyword argument (*args) in isolation ──────
print("\n--- 1. *args in isolation ---")

def testFunction_args_only(*args):
    print(args, type(args))

testFunction_args_only(10, 20, 30, 40)
testFunction_args_only()

# ── 2. Positional parameters before *args ────────────────────
print("\n--- 2. Positional params before *args ---")

def testFunction_positional(a, b, c, *args):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")

testFunction_positional(10, 20, 30)
testFunction_positional(10, 20, 30, 40)
testFunction_positional(10, 20, 30, 40, [100, 200, 300])
testFunction_positional(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160)

# ── 3. Keyword-only arguments after *args ────────────────────
print("\n--- 3. Keyword-only arguments after *args ---")

def testFunction_kwonly(a, b, c, *args, p, q):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"p={p}, q={q}")

# This would fail: testFunction_kwonly(10, 20, 30, 40, 50, 60, 70, 80, 90)
# TypeError: missing 2 required keyword-only arguments: 'p' and 'q'
print("Calling with p and q as keyword arguments:")
testFunction_kwonly(10, 20, 30, 40, 50, 60, 70, p=80, q=90)

# ── 4. Default arguments ────────────────────────────────────
print("\n--- 4. Default arguments ---")

def testFunction_default(a=10, b=20, c=30):
    print(f"a={a}, b={b}, c={c}")

testFunction_default()
testFunction_default(a=100)
testFunction_default(100)
testFunction_default(10, 20, 300)
testFunction_default(c=300)

# ── 5. Integrating default with positional, *args, keyword-only ──
print("\n--- 5. Default + positional + *args + keyword-only ---")

def testFunction_integrated(a, b, c, *args, x=1.1, y=2.2, p, q):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"x={x}, y={y}")
    print(f"p={p}, q={q}")

testFunction_integrated(10, 20, 30, 40, 50, 60, 70, y=20.25, p=False, q=True)

# ── 6. Extra keyword arguments (**kwargs) in isolation ───────
print("\n--- 6. **kwargs in isolation ---")

def testFunction_kwargs_only(**kwargs):
    print(kwargs)

testFunction_kwargs_only()
testFunction_kwargs_only(a=10, b=20, c=30)

# ── 7. MasterFunction: all parameter types combined ─────────
print("\n--- 7. MasterFunction: all parameter types ---")

def MasterFunction(a, b, c, *args, x=1.1, y=2.2, p, q, **kwargs):
    print("Positional arguments")
    print(f"  a:{a}, b:{b}, c:{c}")
    print("Extra non-keyword arguments")
    for i in range(len(args)):
        print(f"  args[{i}]:{args[i]}")
    print("Default arguments")
    print(f"  x:{x}, y:{y}")
    print("Keyword only arguments")
    print(f"  p:{p}, q:{q}")
    print("Extra-keyword arguments")
    for key, val in kwargs.items():
        print(f"  {key} {val}")

MasterFunction(10, 20, 30, 40, 50, 60, 70, y=20.25, p=False, q=True, u=False, w=True, v=False)

# ── 8. Non-Default-After-Default rule ────────────────────────
print("\n--- 8. Non-default after default rule ---")

def testFunction_no_args(a, b, c, x=1.1, y=2.2):
    print(f"a={a}, b={b}, c={c}")
    print(f"x={x}, y={y}")

testFunction_no_args(10, 20, 30, y=20.25)
testFunction_no_args(10, b=20, c=30, y=20.25)

# This would be a SyntaxError:
# def testFunction(a, b, c, x=1.1, y=2.2, p, q):
#     SyntaxError: parameter without a default follows parameter with a default

print("\nWorkaround using **kwargs instead of keyword-only params:")

def testFunction_workaround(a, b, c, x=1.1, y=2.2, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"x={x}, y={y}")
    print(f"kwargs={kwargs}")

testFunction_workaround(10, 20, 30, y=20.25)

print("\n" + "=" * 60)
print("SESSION 088 COMPLETE")
print("=" * 60)
