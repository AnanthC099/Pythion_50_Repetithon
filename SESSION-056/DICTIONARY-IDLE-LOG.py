Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Dictionary Data Type - In Depth Study
# Step 1: Ways of creation
# Way 1: Special Syntax:
D1 = {'a' : 10, 'b' : 20, 'c' : 30}
# Key of dictionary can be any immutable object
D2 = {True:100, 10:200, 1.1:300, "Hello":400, (-1,-2,-3):500}
v1 = D2[True] # v1 == 100
v2 = D2[10]     # v2 = 200
v3 = D2[1.1]    # v3 == 300
v4 = D2["Hello"] # v4 == 400
v5 = D2[(-1, -2, -3)] # v5 == 500
print(v1, v2, v3, v4, v5)
100 200 300 400 500
# Way 2: Constructor Syntax
# Version 1
D3 = dict(p=1.1, q=2.2, r=3.3)
print(D3)
{'p': 1.1, 'q': 2.2, 'r': 3.3}
# Version 2: When all keys are present in one container and all values are present in another container
L1 = ['a', 'b', 'c', 'd']
L2 = [1000, 2000, 3000, 4000]
z = zip(L1, L2)
type(z)
<class 'zip'>
print(z)
<zip object at 0x0000012FE8CF97C0>
for t in z:
    print(t, type(t))

    
('a', 1000) <class 'tuple'>
('b', 2000) <class 'tuple'>
('c', 3000) <class 'tuple'>
('d', 4000) <class 'tuple'>
z = zip(L1, L2)
D = dict(z)
D
{'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}
D = dict(zip(['a', 'b', 'c', 'd'], [1000, 200, 300, 400]))
D
{'a': 1000, 'b': 200, 'c': 300, 'd': 400}
# Way 3: There is static method named 'fromkeys' in class 'dict'
D = dict.fromkeys(['a', 'b', 'c', 'd'])
print(D)
{'a': None, 'b': None, 'c': None, 'd': None}
D = dict.fromkeys(['a', 'b', 'c', 'd'], 0)
D
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
D = dict.fromkeys(['a', 'b', 'c', 'd'], 8)
D
{'a': 8, 'b': 8, 'c': 8, 'd': 8}
@# way 4: Dictionary Comprehension (to be covered at the time of functional programming)
SyntaxError: invalid syntax
#-----------------------------------------------------------------------------

# Step 2: Operators on dictionary
# Subscript operator
D = {'a':10, 'b':20, 'c':30}
v = D['a']
print(v)
10
# Membership testing operator for keys (not for values)
'a' in D
True
10 in D
False
# Step 3: Built in functions
D = {'a': 10, 'b': 20, 'c': 30}
print(D)
{'a': 10, 'b': 20, 'c': 30}
len(D)
3
id(D)
1305283890624
>>> type(D)
<class 'dict'>
>>> # Step 4: Class methods
>>> # Dictionary views: 1) Key view, 2) Value view, 3) Item views
>>> D = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
>>> K = D.keys()
>>> V = D.values()
>>> I = D.items()
>>> type(K)
<class 'dict_keys'>
>>> type(V)
<class 'dict_values'>
>>> type(I)
<class 'dict_items'>
>>> print(K)
dict_keys(['a', 'b', 'c', 'd'])
>>> print(V)
dict_values([10, 20, 30, 40])
>>> print(I)
dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
>>> for k in D.keys():
...     print(k)
... 
...     
a
b
c
d
>>> for v in D.values():
...     print(v)
... 
...     
10
20
30
40
>>> for t in D.items():
    print(t)

    
('a', 10)
('b', 20)
('c', 30)
('d', 40)
L = [10, 20, 30, 40]
for x in L:
    print(x)

    
10
20
30
40
L = [10, 20, (30, 40), 50]
for x in L:
    print(x)

    
10
20
(30, 40)
50
L = [(10, 20, 30), (40, 50, 60), (70, 80, 90), (100, 110, 120)]
for t in L:
    print(t, type(t), len(t))

    
(10, 20, 30) <class 'tuple'> 3
(40, 50, 60) <class 'tuple'> 3
(70, 80, 90) <class 'tuple'> 3
(100, 110, 120) <class 'tuple'> 3
for (x, y, z) in L:
    print(x, y, z)

    
10 20 30
40 50 60
70 80 90
100 110 120
for (key, value) in D.items():
    print(key, value)

    
a 10
b 20
c 30
d 40
for (kajol, twinkle) in D.items():
    print(kajol, twinkle)

    
a 10
b 20
c 30
d 40
(key, value) = ('a', 10)
key
'a'
value
10
(key, value) = ('b', 20)
key
'b'
v
valye
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    valye
NameError: name 'valye' is not defined. Did you mean: 'value'?
value
20
