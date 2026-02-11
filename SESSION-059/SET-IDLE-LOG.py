Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #--------SET DATA TYPE IN-DEPTH STUDY------------
>>> # Ways of creation
>>> # 1: Special syntax
>>> S = {10, 20, 30, 40} #
>>> # IMPORTANT POINT: SET CAN CONTAIN ONLY IMMUTABLE OBJECTS
>>> S = {True, 10, 3.14, "Hello", (100, 200, 300)}
>>> print(S)
{True, 3.14, (100, 200, 300), 10, 'Hello'}
>>> type(S)
<class 'set'>
>>> L = [10, 20, 30, 40]
>>> L.remove(20)
>>> L
[10, 30, 40]
>>> L.remove(50)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    L.remove(50)
ValueError: list.remove(x): x not in list
>>> S = {100, 200, 300, 400}
>>> type(S)
<class 'set'>
>>> S.remove(200)
>>> print(S)
{100, 300, 400}
>>> S.remove(500)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    S.remove(500)
KeyError: 500
>>> #-----------------------------------
>>> # 2: Special syntax ( additional point)
>>> # How to creat an empty set?
>>> S = { }
>>> type(S)
<class 'dict'>
# Empty set cannot be created using special syntax
# Because empty {} -> is inferred as a dictionary object by Python
# Threefore you must use the constructor syntax
S = set()
len(S)
0
print(S)
set()
L = []
print(L)
[]
T = ()
print(T)
()
D = {}
print(D)
{}
S = set()
print(S)
set()
S = 'ABCD'
L = [10, 20, 30, 40]
T= (100, 200, 30)
S1 = set(S)
S2 = set(L)
S3 = set(T)
print(S1)
{'C', 'A', 'B', 'D'}
print(S2)
{40, 10, 20, 30}
print(S3)
{200, 100, 30}
s
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s
NameError: name 's' is not defined. Did you mean: 'S'?
'
s = 'MISSISSIPPI'
S = set(s)
print(S)
{'P', 'M', 'I', 'S'}
set(s)
{'P', 'M', 'I', 'S'}
len(set(s))
4
s = "MISSISSIPPI"
D = dict.fromkeys(set(s))
D = dict.fromkeys(set(s), 0)
D
{'P': 0, 'M': 0, 'I': 0, 'S': 0}
for c in s:
    D[c] += 1

    
D
{'P': 2, 'M': 1, 'I': 4, 'S': 4}
# set comprehension
S = {x for x in range(10)}
print(S)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
