Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Operators that compatible with set
S = {10, 20, 30, 40}
# membership testing in operator
10 in S
True
b = (20 in S)
print(b)
True
b = (500 in S)
print(b)
False
S[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    S[0]
TypeError: 'set' object is not subscriptable
S['a']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    S['a']
TypeError: 'set' object is not subscriptable
print(S)
{40, 10, 20, 30}
# Set object is not sequential. It is not associative. But it supports iterator
for x in S:
    print(x)

    
40
10
20
30
# Operators applicable on set object --- DONE
# PART 3 ->  Built in functions compatible with set object
S = {10, 20, 30, 40}
print(S)
{40, 10, 20, 30}
type(S)
<class 'set'>
len(S)
4
id(S)
1160702268960
# PART 4 -> class methods which compatible with set object
S1 = {10, 20, 30, 40}
S2 = {30, 40, 50, 60}
# Immutable union
S3 = S1.union(S2)
print(S1)
{40, 10, 20, 30}
print(S2)
{40, 50, 60, 30}
print(S3)
{40, 10, 50, 20, 60, 30}
id(S1)
1160702269184
id(S2)
1160701488576
id(S3)
1160702270304
# Immutable intersection
print(S)
{40, 10, 20, 30}
print(S2)
{40, 50, 60, 30}
S3 = S1.intersection(S2)
print(S1)
{40, 10, 20, 30}
print(S2)
{40, 50, 60, 30}
print(S3)
{40, 30}
# Immutable difference
print(S1)
{40, 10, 20, 30}
print(S2)
{40, 50, 60, 30}
S3 = S1.difference(S2)
print(S1)
{40, 10, 20, 30}
print(S2)
{40, 50, 60, 30}
print(S3)
{10, 20}
S4 = S2.difference(S1)
print(S4)
{50, 60}
# Immutable symmetric difference
S4 = S1.symmetric_difference(S2)
print(S1)
{40, 10, 20, 30}
print(S2)
{40, 50, 60, 30}
print(S4)
{10, 50, 20, 60}
# Mutable union
S1 = {10, 20, 30, 40}
S2 = {30, 40, 50, 60}
S1.update(S2) # update() -> union_update()
print(S2)
{40, 50, 60, 30}
print(S1)
{40, 10, 50, 20, 60, 30}
# Restore S1
S1 = {10, 20, 30, 40}
S2.update(S1)
print(S1)
{40, 10, 20, 30}
print(S2)
{40, 10, 50, 20, 60, 30}
# Restore
S3 = {30, 40, 50, 60}
# Mutable intersection
print(S1)
{40, 10, 20, 30}
print(S2)
{40, 10, 50, 20, 60, 30}
# Discrad last three lines
# Restore S2
S2 = {30, 40, 50, 60}
# Mutable Intersection
print(S1)
{40, 10, 20, 30}
print(S2)
{40, 50, 60, 30}
S1.intersection_update(S2)
print(S2)
{40, 50, 60, 30}
print(S1)
{40, 30}
# Restore S1
S1 = {10, 20, 30, 40}
# Mutable difference
S1.difference_update(S2)
print(S2)
{40, 50, 60, 30}
print(S1)
{20, 10}
# Restore S1
S1 = {10, 20, 30, 40}
S2.difference_update(S1)
print(S1)
{40, 10, 20, 30}
print(S2)
{50, 60}
# Restore S2
S2 = {30, 40, 50, 60}
S1.symmetric_difference_update(S2)
print(S1)
{10, 50, 20, 60}
print(S2)
{40, 50, 60, 30}
# 3 Query functions
S1 = {10, 20, 30, 40}
S2 = {10, 20, 30, 40, 50}
S1.issubset(S2)
True
S2.issuperset(S1)
True
S2.issubset(S2)
True
S1.issubset(S1)
True
S2.issubset(S1)
False
S1.issuperset(S2)
False
S1.issuperset(S1)
True
S2.issuperset(S2)
True
S1.isdisjoint(S2)
False
S1 = {10, 20, 30, 40, 50}
S2 = {1.1, 2.2, 3.3, 4.4, 5.5}
S1.isdisjoint(S2)
True
# Set management function
# How to add data in set
# Let us start with an empty set
S = set()
print(S)
set()
type(S)
<class 'set'>
len(S)
0
# add function
S.add(True)
print(S)
{True}
S.add(10)
print(S)
{True, 10}
S.add(3.14)
print(S)
{True, 10, 3.14}
S.add("Hello")
print(S)
{True, 10, 3.14, 'Hello'}
S.add((100, 200, 300))
print(S)
{True, 3.14, (100, 200, 300), 10, 'Hello'}
# How to remove elements from set
# method: remove()
S = {10, 20, 30, 40}
S.remove(20)
print(S)
{40, 10, 30}
S.remove(10)
S
{40, 30}
S.remove(500) # non existent data will trigger an exception
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    S.remove(500) # non existent data will trigger an exception
KeyError: 500
# method: discard() -> Leninent version of remove
>>> # If the element exists then discard() function removes it from the set
>>> # if the element does not exist discard() function does not trigger any exception, it silently returns
>>> S = {10, 20, 30, 40}
>>> print(S)
{40, 10, 20, 30}
>>> S.remove(20)
>>> print(S)
{40, 10, 30}
>>> S.discard(30)
>>> print(S)
{40, 10}
>>> S.discard(500)
>>> print(S)
{40, 10}
>>> S = {10,20,30,40}
>>> ret = S.pop()
>>> print(ret)
40
>>> print(S)
{10, 20, 30}
>>> ret = S.pop()
>>> print(ret)
10
>>> S
{20, 30}
>>> ret = S.pop()
>>> print(S)
{30}
>>> ret
20
>>> # method: clear()
>>> # If you want to remove all elements in set S
>>> S = {10, 20, 30, 40, 50}
>>> S = set() # WRONG !!
>>> S = {10, 20, 30, 40, 50}
>>> S.clear() # CORRECT !!
