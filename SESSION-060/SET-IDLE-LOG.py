# SET-IDLE-LOG.py
# Converted from IDLE session log to executable Python script
# Topic: Set operations in Python

# ---- PART 2: Operators compatible with set ----

S = {10, 20, 30, 40}

# Membership testing with 'in' operator
print("10 in S:", 10 in S)
b = (20 in S)
print("20 in S:", b)
b = (500 in S)
print("500 in S:", b)

# Set is not subscriptable (no indexing)
try:
    S[0]
except TypeError as e:
    print("S[0] ->", e)

try:
    S['a']
except TypeError as e:
    print("S['a'] ->", e)

print("print(S):", S)

# Set object is not sequential. It is not associative. But it supports iterator
print("Iterating over S:")
for x in S:
    print(x)

# ---- PART 3: Built-in functions compatible with set object ----
S = {10, 20, 30, 40}
print("\nprint(S):", S)
print("type(S):", type(S))
print("len(S):", len(S))
print("id(S):", id(S))

# ---- PART 4: Class methods compatible with set object ----

S1 = {10, 20, 30, 40}
S2 = {30, 40, 50, 60}

# Immutable union
S3 = S1.union(S2)
print("\n--- Immutable union ---")
print("S1:", S1)
print("S2:", S2)
print("S1.union(S2):", S3)
print("id(S1):", id(S1), "id(S2):", id(S2), "id(S3):", id(S3))

# Immutable intersection
S3 = S1.intersection(S2)
print("\n--- Immutable intersection ---")
print("S1:", S1)
print("S2:", S2)
print("S1.intersection(S2):", S3)

# Immutable difference
S3 = S1.difference(S2)
print("\n--- Immutable difference ---")
print("S1:", S1)
print("S2:", S2)
print("S1.difference(S2):", S3)
S4 = S2.difference(S1)
print("S2.difference(S1):", S4)

# Immutable symmetric difference
S4 = S1.symmetric_difference(S2)
print("\n--- Immutable symmetric difference ---")
print("S1:", S1)
print("S2:", S2)
print("S1.symmetric_difference(S2):", S4)

# Mutable union
S1 = {10, 20, 30, 40}
S2 = {30, 40, 50, 60}
S1.update(S2)  # update() -> union_update()
print("\n--- Mutable union (update) ---")
print("S2:", S2)
print("S1 after S1.update(S2):", S1)

# Restore S1
S1 = {10, 20, 30, 40}
S2 = {30, 40, 50, 60}

# Mutable Intersection
print("\n--- Mutable intersection (intersection_update) ---")
print("S1:", S1)
print("S2:", S2)
S1.intersection_update(S2)
print("S1 after S1.intersection_update(S2):", S1)
print("S2:", S2)

# Restore S1
S1 = {10, 20, 30, 40}

# Mutable difference
S1.difference_update(S2)
print("\n--- Mutable difference (difference_update) ---")
print("S1 after S1.difference_update(S2):", S1)
print("S2:", S2)

# Restore S1
S1 = {10, 20, 30, 40}
S2.difference_update(S1)
print("\nS2 after S2.difference_update(S1):", S2)
print("S1:", S1)

# Restore S2
S2 = {30, 40, 50, 60}
S1.symmetric_difference_update(S2)
print("\n--- Mutable symmetric difference (symmetric_difference_update) ---")
print("S1 after S1.symmetric_difference_update(S2):", S1)
print("S2:", S2)

# ---- 3 Query functions ----
S1 = {10, 20, 30, 40}
S2 = {10, 20, 30, 40, 50}
print("\n--- Query functions ---")
print("S1:", S1)
print("S2:", S2)
print("S1.issubset(S2):", S1.issubset(S2))
print("S2.issuperset(S1):", S2.issuperset(S1))
print("S2.issubset(S2):", S2.issubset(S2))
print("S1.issubset(S1):", S1.issubset(S1))
print("S2.issubset(S1):", S2.issubset(S1))
print("S1.issuperset(S2):", S1.issuperset(S2))
print("S1.issuperset(S1):", S1.issuperset(S1))
print("S2.issuperset(S2):", S2.issuperset(S2))
print("S1.isdisjoint(S2):", S1.isdisjoint(S2))

S1 = {10, 20, 30, 40, 50}
S2 = {1.1, 2.2, 3.3, 4.4, 5.5}
print("S1.isdisjoint(S2) (disjoint sets):", S1.isdisjoint(S2))

# ---- Set management functions ----
print("\n--- Set management functions ---")

# Starting with an empty set
S = set()
print("Empty set:", S)
print("type(S):", type(S))
print("len(S):", len(S))

# add function
S.add(True)
print("After S.add(True):", S)
S.add(10)
print("After S.add(10):", S)
S.add(3.14)
print("After S.add(3.14):", S)
S.add("Hello")
print("After S.add('Hello'):", S)
S.add((100, 200, 300))
print("After S.add((100, 200, 300)):", S)

# How to remove elements from set
print("\n--- Removing elements ---")

# method: remove()
S = {10, 20, 30, 40}
S.remove(20)
print("After S.remove(20):", S)
S.remove(10)
print("After S.remove(10):", S)

try:
    S.remove(500)  # non existent data will trigger an exception
except KeyError as e:
    print("S.remove(500) -> KeyError:", e)

# method: discard() -> Lenient version of remove
# If the element exists then discard() removes it from the set
# If the element does not exist discard() does not trigger any exception
S = {10, 20, 30, 40}
print("\nS:", S)
S.remove(20)
print("After S.remove(20):", S)
S.discard(30)
print("After S.discard(30):", S)
S.discard(500)
print("After S.discard(500) (no error):", S)

# method: pop()
S = {10, 20, 30, 40}
ret = S.pop()
print("\nS.pop() returned:", ret, "| S:", S)
ret = S.pop()
print("S.pop() returned:", ret, "| S:", S)

# method: clear()
# Remove all elements in set S
S = {10, 20, 30, 40, 50}
print("\nBefore clear:", S)
S.clear()
print("After S.clear():", S)
