Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Study of build in data types.
>>> # How to study a built in data types in four steps?
>>> # STEP 1: Learn all ways to create an object from data type.
>>> # STEP 2: Study the built in operators that can be applied on the objects of data type.
>>> # STEP 3: Study the built in functions with which object of data type are compatible.
>>> # STEP 4: Study class methods that can be applied on the object of data type.
>>> # 1) List data type
>>> # STEP 1 : Ways of creation
>>> # Use special syntax
>>> L = [10, 20, 30, 40]
>>> # list can contain objects of different type at each index
>>> L1 = [True, 10, 3.14, "Hello"]
>>> # List can contain other containers as members
>>> L2 = ["Hello", [100, 200, 300], (1, 2, 3), {'a':10, 'b':20}, {-1, -2, -3}]
>>> print(L)
[10, 20, 30, 40]
>>> print(L1)
[True, 10, 3.14, 'Hello']
>>> print(L2)
['Hello', [100, 200, 300], (1, 2, 3), {'a': 10, 'b': 20}, {-3, -2, -1}]
>>> # Method 2: Constructor syntax: Used to create list from other containers
>>> s1 = "ABC"
>>> T = (100, 200, 300)
>>> S = {-1, -2, -3, -4}
>>> L1 = list(s1)
>>> L2 = list(T)
>>> L3 = list(S)
>>> print(L1)
['A', 'B', 'C']
>>> print(L2)
[100, 200, 300]
>>> print(L3)
[-4, -3, -2, -1]
>>> print(s1)
ABC
print(T)
(100, 200, 300)
print(S)
{-4, -3, -2, -1}
# Method 3: List comprehension -> Will be covered while teaching functional programming part of Python
# Create a list of square of all even numbers between 1 to 50
L1 = []
i = 1
while i <= 50:
    if i % 2 == 0:
        L1.append(i**2)
    i = i + 1

    
L1
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500]
# See the magic of list comprehension
L2 = [x**2 for x in range(1, 51) if x % 2 == 0]
L2
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500]
#-------------------------STEP 1 COMPLETE
# STEP 2: Built in operators on list
# 1. Concatenation
L1 = [10, 20, 30, 40]
L2 = [50, 60, 70, 80]
L3 = L1 + L2
print(L3)
[10, 20, 30, 40, 50, 60, 70, 80]
print(L1)
[10, 20, 30, 40]
print(L2)
[50, 60, 70, 80]
L3 = L1 + L2 + [100, 200, 300] + ['a', 'b', 'c']
print(L3)
[10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 300, 'a', 'b', 'c']
# 2. Multiplication by integer
L1 = [10, 20, 30, 40]
L1 + L1
[10, 20, 30, 40, 10, 20, 30, 40]
L1 + L1 + L1
[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
L1 + L1 + L1 + L1 + L1
[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
L1 * 5
[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
L1 * 50
[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
# General Syntax result_L = L * n
# n must be a non-negative integer
# 3. Index, range, slice [Index operation has been covered, range and slice will be convered in a dedicated lecture
# 4. Membership testing
L = [True, 10, 3.14, "Hello"]
True in L
True
10 in L
True
bPresent = (10 in L)
print(bPresent)
True
bPresent = (-10 in L)
print(bPresent)
False
#-----------------------STEP 2 END
# STEP 3: Built in functions compatible with list object
L = [10, 20, 30, 40, 50]
print(L)
[10, 20, 30, 40, 50]
type(L)
<class 'list'>
id(L)
2921886572288
len(L)
5
#--------------------STEP 3 END
# STEP 4: Class methods in list
# method: index()
L = [10, 20, 30, 40, 50]
# Index opeator takes from index to element
L[1]
20
# Index method takes us from element to index
L.index(20)
1
# Non-existent element will trigger a ValueError exception
L.index(500)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    L.index(500)
ValueError: list.index(x): x not in list
# method: count()
L = [10, 20, 30, 10, 40, 20, 10, 50, 60, 10]
L.count(10)
4
L.count(20)
2
L.count(50)
1
L.count(-1)
0
# insertion techniques: How to add data to a list
# method: append()
# Append function can be used to add an atomic object or a container object to a list
# If we use a container object with the append method, it gets added as a single object
# Therefore, no matter how many elements are present in the container object, appending it
# would increase the list length only by 1.

# Let us start with an empty list
L = []
print(L)
[]
# Add object of atomic class Bool to L
L.append(True)
L
[True]
# Add integer 10 to L
L.append(10)
len(L)
2
T = (100, 200, 300, 400, 500, 600)
len(T)
6
# Add tuple T to L
L.append(T)
len(L)
3
L
[True, 10, (100, 200, 300, 400, 500, 600)]

# method: extend()
# extend() method accepts a container object. And it adds all top-level elements in the list
# as a separate objects. Therefore, the length of the list is incremented by the length of the container
# If that container itself contains more containers then their elements are not separately added.
# extend() method DOES NOT ACCEPT ATOMIC OBJECT.

# Experiment 1: extend() does not accept atomic objects
L = [10, 20, 30]
L.extend(True)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    L.extend(True)
TypeError: 'bool' object is not iterable
L.extend(40)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    L.extend(40)
TypeError: 'int' object is not iterable
L.extend(1.1)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    L.extend(1.1)
TypeError: 'float' object is not iterable

# Experiment 2: extend() adds elements in container separately
L
[10, 20, 30]
T
(100, 200, 300, 400, 500, 600)
L.extend(T)
L
[10, 20, 30, 100, 200, 300, 400, 500, 600]
len(L)
9

# Experiment 3: extend() does not separate container within containers
L = [10, 20, 30]
L
[10, 20, 30]
T = ( (100, 200, 300), (400, 500, 600), (700, 800, 900) )
T[0]
(100, 200, 300)
T[1]
(400, 500, 600)
T[2]
(700, 800, 900)
T
((100, 200, 300), (400, 500, 600), (700, 800, 900))
len(L)
3
L.extend(T)
L
[10, 20, 30, (100, 200, 300), (400, 500, 600), (700, 800, 900)]

==== RESTART: C:/Users/yoges/OneDrive/Documents/CPA/PYTHON/BATCH_CODES/BATCH_50/SESSION-054/add-separate.py ===
[]
[10, 20, 30, 40, 50, 60, 70, 100, 200, 300, 400, 500]
# insert() function
# General Syntax: L.insert(index, element)
# insert() method, inserts given @element at given @index

# Prevailant view
# insert() method inserts data before given index
L = [10, 20, 30, 40, 50, 60]
# find index of 40
L.index(40)
3
L.insert(3, -1)
L
[10, 20, 30, -1, 40, 50, 60]
# Discard Prevaialant view ( -> BALISH)

