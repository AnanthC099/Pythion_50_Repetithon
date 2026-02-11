# IDLE-LOG-SHALLOW-AND-DEEP-COPYING.py
# Converted from IDLE session log to executable Python script
# Topic: Shallow and Deep Copying in Python

import copy

# ---- Assignment is aliasing, not copying ----
print("--- Assignment is aliasing ---")
b1 = True
b2 = b1
print("id(b1):", id(b1))
print("id(b2):", id(b2))
print("b1 is b2:", b1 is b2)

L1 = [10, 20, 30]
L2 = L1
print("\nid(L1):", id(L1))
print("id(L2):", id(L2))
print("L1 is L2:", L1 is L2)

# ---- Implicit cloning of immutable objects ----
print("\n--- Implicit cloning of immutable objects ---")
n = 1.1
m = 1.1
print("m:", m)
print("n:", n)
print("id(m):", id(m))
print("id(n):", id(n))
print("m == n:", m == n)
print("m is n:", m is n)

# ---- Explicit cloning using copy method (shallow copy) ----
print("\n--- Shallow copy using .copy() method ---")

# List copy
L = [10, 20, 30]
L1 = L.copy()
print("L == L1:", L == L1)
print("L:", L)
print("L1:", L1)
print("id(L):", id(L))
print("id(L1):", id(L1))
print("L is L1:", L is L1)

# Dict copy
D1 = {'a': 10, 'b': 20, 'c': 30}
D2 = D1.copy()
print("\nid(D1):", id(D1))
print("id(D2):", id(D2))
print("D1 == D2:", D1 == D2)
print("D1 is D2:", D1 is D2)

# Set copy
S1 = {100, 200, 300}
S2 = S1.copy()
print("\nS1 == S2:", S1 == S2)
print("S1 is S2:", S1 is S2)

# Immutable types do NOT have .copy()
print("\n--- Immutable types do NOT have .copy() ---")
for obj, name in [(False, 'bool'), (100, 'int'), (1.1, 'float'), ("Hello", 'str'), ((100, 200, 300), 'tuple')]:
    try:
        obj.copy()
    except AttributeError as e:
        print(f"{name}.copy() -> {e}")

# ---- Shallow copy problem with nested mutable objects ----
print("\n--- Shallow copy problem ---")
L1 = [10, 20, 30, 40]
L2 = L1.copy()
print("id(L1):", id(L1))
print("id(L2):", id(L2))
print("L1 is L2:", L1 is L2)
print("L1 == L2:", L1 == L2)

print("\nElement IDs in L1:")
for x in L1:
    print(x, id(x))
print("Element IDs in L2:")
for x in L2:
    print(x, id(x))

# As 10, 20, 30, 40 are all immutable, sharing across L1 & L2 is NOT problematic
# IF A LIST CONTAINS A MUTABLE OBJECT INSIDE IT THEN IT BECOMES PROBLEMATIC
print("\n--- Nested mutable object with shallow copy ---")
L1 = [10, 20, 30, [100, 200, 300], 40]
L2 = L1.copy()
print("id(L1):", id(L1))
print("id(L2):", id(L2))
print("L1 is L2:", L1 is L2)
print("L1 == L2:", L1 == L2)
print("L1[3]:", L1[3])
print("L2[3]:", L2[3])
print("id(L1[3]):", id(L1[3]))
print("id(L2[3]):", id(L2[3]))
print("L1[3] is L2[3]:", L1[3] is L2[3])

L1[3].append(400)
print("\nAfter L1[3].append(400):")
print("L1:", L1)
print("L2:", L2, " <-- L2 also changed!")

# ---- Deep copy solves this problem ----
print("\n--- Deep copy with copy.deepcopy() ---")
L1 = [10, 20, 30, [100, 200, 300], 40]
L2 = copy.deepcopy(L1)
print("id(L1):", id(L1))
print("id(L2):", id(L2))

# Immutable elements still share the same id
print("\nImmutable elements (shared):")
print("id(L1[0]):", id(L1[0]), "id(L2[0]):", id(L2[0]))
print("id(L1[1]):", id(L1[1]), "id(L2[1]):", id(L2[1]))
print("id(L1[2]):", id(L1[2]), "id(L2[2]):", id(L2[2]))

# Mutable nested list gets its own copy
print("\nMutable nested list (independent copies):")
print("id(L1[3]):", id(L1[3]))
print("id(L2[3]):", id(L2[3]))
print("L1[3] is L2[3]:", L1[3] is L2[3])

L1[3].append(400)
print("\nAfter L1[3].append(400):")
print("L1:", L1)
print("L2:", L2, " <-- L2 NOT affected!")
print("L1[3]:", L1[3])
print("L2[3]:", L2[3])
