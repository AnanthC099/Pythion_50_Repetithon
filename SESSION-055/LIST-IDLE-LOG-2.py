Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# List data type continued. . .
# method: insert()
# General Syntax: L.insert(index, element)
# Interpretation: Insert given element at given index.
# If there is a data already present at given index then required rearrangement of data
# will be carried out by the insert() function.
L = [10, 20, 30, 40, 50, 60]
L[2]
30
L.insert(2, -1) # index = 2, element=-1 -> -1 will be inserted at index 2
print(L)
[10, 20, -1, 30, 40, 50, 60]
# Insert at the beginning.
# Insert element -1 at the start of the list
L.insert(0, -1) # index = 0, Element = -1
print(L)
[-1, 10, 20, -1, 30, 40, 50, 60]
# Insert at the end
# Insert element -1 at the end of the list
L.insert(len(L), -1)
print(L)
[-1, 10, 20, -1, 30, 40, 50, 60, -1]
# Insert new element after GIVEN ELEMENT
L
[-1, 10, 20, -1, 30, 40, 50, 60, -1]
# Example: Insert element -1 after 40
# L.index(40) -> will give you index of element 40
# L.insert(L.index(40) + 1, -1)
L.insert(L.index(40) + 1, -1)
# Insert new element BEFORE GIVEN ELEMENT
# Example: Insert element -1 before 40
L.insert(L.index(40), -1)
L
[-1, 10, 20, -1, 30, -1, 40, -1, 50, 60, -1]
# General Patters:
# Insert at start: L.insert(0, element)
# Insert at end: L.insert(len(L), element)
# Insert after data: L.insert(L.index(data), element)
# PREVIOUS COMMENT IS WRONG-> CORRECTING IT BELOW
# Insert after data: L.insert(L.index(data) + 1, element)
# Insert before data: L.insert(L.index(data), element)

# Modification methods: index based modification, range based modification, slice based modification
# range and slice based modifications will be covered later
L = [10, 20, 30, 40, 50, 60]
L[1] = 200
# General format of index based modification: L[valid_index] = new_element

# Data removal methods:
# 1) index based deletion 2) range based deletion 3) slice based deletion
# 4) remove() 5) pop() 6) clear()
# We will not cover range based deletion and slice based deletion now.
L = [10, 20, 30, 40, 50, 60, 70]
L[2]
30
del L[2]
L
[10, 20, 40, 50, 60, 70]
# General format of index based deletion: del L[valid_index]

# method: remove() -> data based removal
L
[10, 20, 40, 50, 60, 70]
L.remove(40)
L
[10, 20, 50, 60, 70]
# General formal: L.remove(existing_element)
L.remove(500)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    L.remove(500)
ValueError: list.remove(x): x not in list

# method: pop()
L = [10, 20, 30, 40, 50, 60, 70]
n = L.pop(3)
L
[10, 20, 30, 50, 60, 70]
print(n)
40
L
[10, 20, 30, 50, 60, 70]
n = L.pop()
L
[10, 20, 30, 50, 60]
n
70

# method: clear() : How to clear all elements from a given list
# PREVAILANT PRACTICE: L = [] to drop all elements from a given list
# This syntax creates a new list object and reassigns variable L to it.
# Old list object is detached from L, its reference count is decremented by 1.
# If it falls down to 0 then using this wrong practice WILL NOT COST MUCH.
# But in case it does not then you not only keep the old list intact in memory
# but also end up creating a new empty list object. In no universe, this or parallel,
# this is how a removal of all elements is implemented !
# clear() method removes all elements on the calling object.
L = [10, 20, 30, 40, 50, 60]
id(L)
2155601102848
L.clear()
L
[]
id(L)
2155601102848
L1 = [10, 20, 30, 40, 50]
L2 = L1
id(L1)
2155555843968
id(L2)
2155555843968
L1.clear()
id(L1)
2155555843968
id(L2)
2155555843968
>>> L1
[]
>>> L2
[]
>>> 
>>> #-----------------------------------REMOVAL METHODS DONE
>>> 
>>> # MISCALLANEOUS FUNCTIONS: 1) revese() 2) sort() 3) copy()
>>> 
>>> # method: reverse() : It RE-ARRANGES given elements in the list in the reverse order
>>> L = [10, 20, 40, 20, 60]
>>> print(L)
[10, 20, 40, 20, 60]
>>> L.reverse()
>>> L
[60, 20, 40, 20, 10]
>>> 
>>> M = [10, 20, 30, 40]
>>> N = M[::-1] # This is an advanced slice syntax
>>> print(M)
[10, 20, 30, 40]
>>> print(N)
[40, 30, 20, 10]
>>> id(M)
2155600897600
>>> id(N)
2155601061888
>>> 
>>> #----------------------------------------------------
>>> L = [20, 10, 30, 40, 50]
>>> L_sorted = sorted(L)
>>> L_sorted
[10, 20, 30, 40, 50]
>>> L
[20, 10, 30, 40, 50]
>>> L_sorted
[10, 20, 30, 40, 50]
method: sort()
:
    
SyntaxError: invalid syntax
L
[20, 10, 30, 40, 50]
# method: sort()
L
[20, 10, 30, 40, 50]
L.sort()
L
[10, 20, 30, 40, 50]
id(L)
2155555834816
print(L)
[10, 20, 30, 40, 50]
type(L)
<class 'list'>
sorted(L)
[10, 20, 30, 40, 50]


L = [10, 20, 30]
print(L)
[10, 20, 30]
M = L[::-1]
print(M)
[30, 20, 10]
print(L)
[10, 20, 30]
L = [20, 10, 30, 40]
print(L)
[20, 10, 30, 40]
M = sorted(L)
print(M)
[10, 20, 30, 40]
print(L)
[20, 10, 30, 40]


L = [10, 20, 30, 40]
print(L)
[10, 20, 30, 40]
L.reverse()
print(L)
[40, 30, 20, 10]
L = [20, 10, 30, 40]
print(L)
[20, 10, 30, 40]
L.sort()
print(L)
[10, 20, 30, 40]
#----------------------------------------------
