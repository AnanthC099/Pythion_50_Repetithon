"""
Session 087: Parameter Passing — Introduction
Topics covered:
  1. The six types of formal parameters
  2. Non-keyword vs keyword actual-argument syntax
  3. The Golden Rule (keyword syntax cannot revert to non-keyword)
  4. Insight 1 — positional params can be called with keyword syntax
  5. Insight 2 — default params can be called with non-keyword syntax
"""

print("=" * 60)
print("SESSION 087: PARAMETER PASSING — INTRODUCTION")
print("=" * 60)

# ── 1. Positional argument ────────────────────────────────────
print("\n--- 1. Positional argument ---")

def positional_demo(a, b, c):
    print(f"  a={a}, b={b}, c={c}")

positional_demo(10, 20, 30)

print("\n--- 1b. Positional argument with boolean values ---")

def bool_demo(a, b, c, d):
    print(f"  a={a}, b={b}, c={c}, d={d}")

bool_demo(False, True, False, True)

# ── 2. Keyword argument (calling with keyword syntax) ─────────
print("\n--- 2. Keyword argument (calling with keyword syntax) ---")

positional_demo(a=10, b=20, c=30)
positional_demo(c=30, a=10, b=20)   # order doesn't matter with keyword syntax

# ── 3. Extra non-keyword argument (*args) ─────────────────────
print("\n--- 3. Extra non-keyword argument (*args) ---")

def extra_nonkw_demo(a, b, *args):
    print(f"  a={a}, b={b}, args={args}")

extra_nonkw_demo(1, 2)
extra_nonkw_demo(1, 2, 3, 4, 5)

# ── 4. Default argument ───────────────────────────────────────
print("\n--- 4. Default argument ---")

def default_demo(a, b, c=100):
    print(f"  a={a}, b={b}, c={c}")

default_demo(1, 2)         # c takes default value 100
default_demo(1, 2, 3)      # c overridden to 3

# ── 5. Keyword-only argument ──────────────────────────────────
print("\n--- 5. Keyword-only argument (after *args) ---")

def kwonly_demo(a, b, *args, mode):
    print(f"  a={a}, b={b}, args={args}, mode={mode}")

kwonly_demo(1, 2, 3, 4, mode="fast")

# ── 6. Extra keyword argument (**kwargs) ──────────────────────
print("\n--- 6. Extra keyword argument (**kwargs) ---")

def extra_kw_demo(**kwargs):
    print(f"  kwargs={kwargs}")

extra_kw_demo(x=10, y=20, z=30)

# ── Two ways of writing actual parameters ─────────────────────
print("\n" + "=" * 60)
print("TWO WAYS OF WRITING ACTUAL PARAMETERS")
print("=" * 60)

print("\n--- Non-keyword syntax ---")
positional_demo(10, 20, 30)

print("\n--- Keyword syntax ---")
positional_demo(a=10, b=20, c=30)

# ── The Golden Rule ───────────────────────────────────────────
print("\n" + "=" * 60)
print("THE GOLDEN RULE")
print("  Once you start using keyword syntax, you CANNOT")
print("  fall back to non-keyword syntax.")
print("=" * 60)

print("\nValid calls:")
positional_demo(10, 20, 30)         # all non-keyword
positional_demo(10, 20, c=30)       # switch to keyword at c — OK
positional_demo(10, b=20, c=30)     # switch to keyword at b — OK
positional_demo(a=10, b=20, c=30)   # all keyword — OK

print("\nValid call — non-keyword + reordered keyword syntax:")
bool_demo(10, d=40, b=20, c=30)     # keyword args can appear in any order

print("\nInvalid call (would raise SyntaxError):")
print("  positional_demo(a=10, 20, 30)")
print("  # SyntaxError: positional argument follows keyword argument")

# ── INSIGHT 1 ─────────────────────────────────────────────────
print("\n" + "=" * 60)
print("INSIGHT 1: Positional params can be called using keyword syntax")
print("=" * 60)

def insight1_demo(x, y, z):
    print(f"  x={x}, y={y}, z={z}")

print("\nNon-keyword (positional) call:")
insight1_demo(1, 2, 3)

print("Keyword call (same function, same result, different order):")
insight1_demo(z=3, x=1, y=2)

# ── INSIGHT 2 ─────────────────────────────────────────────────
print("\n" + "=" * 60)
print("INSIGHT 2: Default params can be called using non-keyword syntax")
print("=" * 60)

def insight2_demo(a, b=20, c=30):
    print(f"  a={a}, b={b}, c={c}")

print("\nUsing defaults (omit b and c):")
insight2_demo(1)

print("Override defaults with non-keyword syntax:")
insight2_demo(1, 200, 300)

print("Override defaults with keyword syntax:")
insight2_demo(1, c=300)

print("\n" + "=" * 60)
print("SESSION 087 COMPLETE")
print("=" * 60)
