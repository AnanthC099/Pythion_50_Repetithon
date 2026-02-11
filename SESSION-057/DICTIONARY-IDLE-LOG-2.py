Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Dictionary - In Depth Continued
# How to add / modify / remove data from dictionary
# 1) How to add a new key-value pair
# General Format: D[New-Key] = New-Value
D = {}
print(D)
{}
# Dictionary is empty right now. Add key 'a' and value 10 pair
D['a'] = 10
print(D)
{'a': 10}
# To add 'b' : 20 pair, D['b
# D['b'] = 20
D['b'] = 20
print(D)
{'a': 10, 'b': 20}
# Add : True : 1000
D[True] = 1000
print(D)
{'a': 10, 'b': 20, True: 1000}
# Modification:
# Note: 1) You can modify the value of given key
# 2) You cannot modify the key of given valye
# General Format: D[existing_key] = value
D = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
print(D)
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
# Change value associated by key 'b' (from 20 to 200)
D['b'] = 200
print(D)
{'a': 10, 'b': 200, 'c': 30, 'd': 40}
# Change existing value 30 to 300 attached with key 'c'
D['c'] = 300
print(D)
{'a': 10, 'b': 200, 'c': 300, 'd': 40}
# 3) Deletion: How to remove a key value pair from dictionary
# del D[existing_key]
D = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# Remove pair 'a' : 10 from dictionary
del D['a']
print(D)
{'b': 20, 'c': 30, 'd': 40}
# Remove / Delete 'd' : 40 pair from dictionary D
del D['d']
print(D)
{'b': 20, 'c': 30}
# Summary:
# 1) Addition: D[new-key] = value
# 2) Modification: D[existing-key] = value
# 3) Removal: del D[existing-key]
#-------------------------------------------
# additional ways to remove key:value pair(s) from dictionary
# 1) method: popitem()
D = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
print(D)
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
returnValue = D.popitem()
print(returnValue)
('d', 40)
# On empty dictionry, this method will trigger an exception
D1 = {}
type(D1)
<class 'dict'>
print(D1)
{}
D1.popitem()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    D1.popitem()
KeyError: 'popitem(): dictionary is empty'
# 2) method: pop()
D = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40, 'e' : 40}
# The pop method is invoked on the dictionary. The pop method accepts a key from caller
# If the key is not present -> raise KeyError exception
# If the key is present -> Remove the key:value pair from the dictionary and return the value object
# as a return value of pop() function
n = D.pop('c')
print(D)
{'a': 10, 'b': 20, 'd': 40, 'e': 40}
print(n)
30
# 3) clear() : To remove all key-value pairs from a dictionary -> you must invoke a clear function
# WRONG PREVAILANT PRACTIVE: D = {}     -> will clear the dictionary
# Technically speaking D = {} will cause python to allocate a new empty dictionary and assign it to
# variable D. This causes variable D to give up its existing association with the current dictionary.
# This is not equivalent to dropping all key:value pairs from a given dictionary
D = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
id(D)
1731250650944
print(D)
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
D.clear()
id(D)
1731250650944
print(D)
{}
dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# ----------------------
# method: get() : Lenient version of subscript operator on RHS
# Explanation: We use [] operator on dictionary in RHS sense in order to fetch a value associated with any
# key. If the given key is not present in the dictionary then it raises a KeyError exception. If the key is pre# sent it returns the associated value
D = {'a' : 10, 'b' : 20, 'c' : 30}
v = D['b']
print(v)
20
v = D['x']
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    v = D['x']
KeyError: 'x'
# Analyse behaviour of get() method vis-a-vis [] operator on RHS
v = D.get('b')
print(v)
20
# For existing key: get() method behaved similar to [] operator on RHS
v = D.get('x')
print(v)
None
# For non-existent key: get() method returns None instead of triggering an exception
D1 = {'x' : None}
v = D1.get('x')
print(v)
None
v = D1['x']
print(v)
None
#----------------------

# method : setdefault()
# setdefault() function should be considered as a function in the lineage of [] operator on RHS and get()
# method. We have already seen that the get() method is lenient version of [] operator on RHS in a sense that
# get() function does not trigger an exception when presented with non-existent key but [] operator does.

# setdefault() when presented with non-existent key will not only won't trigger an exception but will also
# add non-existent key to the dictionary and attach value None with it and will return None

D
{'a': 10, 'b': 20, 'c': 30}
# For existent key, [] operator on RHS, get() method and setdefault() method behave identically in that
# they return the associated value

D['b']
20
D.get('b')
20
D.setdefault('b')
20

# difference in behaviour when presented with non-existent key
D['x']  # Ancient Indian Parent Like Behaviour
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    D['x']  # Ancient Indian Parent Like Behaviour
KeyError: 'x'
>>> returnValue = D.get('x') # 80's Indian parent
>>> 
>>> v = D.setdefault('x')
>>> D
{'a': 10, 'b': 20, 'c': 30, 'x': None}
>>> v = D.setdefault('y', 100)
>>> D
{'a': 10, 'b': 20, 'c': 30, 'x': None, 'y': 100}
>>> v
100
>>> D
{'a': 10, 'b': 20, 'c': 30, 'x': None, 'y': 100}
>>> D.setdefault('b', 500)
20
>>> D
{'a': 10, 'b': 20, 'c': 30, 'x': None, 'y': 100}
>>> D.setdefault('z', 40)
40
>>> D
{'a': 10, 'b': 20, 'c': 30, 'x': None, 'y': 100, 'z': 40}
>>> D.setdefault('w', 10)
10
>>> D
{'a': 10, 'b': 20, 'c': 30, 'x': None, 'y': 100, 'z': 40, 'w': 10}
>>> # method: update() -> Dictionary's version of concatenation
>>> D1 = {'a' : 10, 'b' : 20, 'c' : 30}
>>> D2 = {'c' : 300, 'd' : 400, 'e' : 500}
>>> D1.update(D2)
>>> D1
{'a': 10, 'b': 20, 'c': 300, 'd': 400, 'e': 500}
>>> D1 = {'a' : 10, 'b' : 20, 'c' : 30}
>>> D2 = {'c' : 300, 'd' : 400, 'e' : 500}
>>> D2.update(D1)
>>> D2
{'c': 30, 'd': 400, 'e': 500, 'a': 10, 'b': 20}
>>> #----------------------------------------------------------------
