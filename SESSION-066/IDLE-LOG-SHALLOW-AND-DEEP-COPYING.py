Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
b1 = True
b2 = b1
id(b1)
140734956161792
id(b2)
140734956161792
L1 = [10, 20, 30]
L2 = L1
id(L1)
2339489160320
id(L2)
2339489160320
#-------------------------
# Mutable objects can be cloned explicitly.
# Implicit cloning
n = 1.1
m = 1.1
print(m)
1.1
print(n)
1.1
id(m)
2339488155184
id(n)
2339488155120
m == n
True
m is n
False
# Explicit cloning using copy method
L = [10, 20, 30]
L1 = L.copy()
L == L1
True
L
[10, 20, 30]
L1
[10, 20, 30]
id(L)
2339489282496
id(L1)
2339489167552
L is L1
False
D1 = {'a' : 10, 'b': 20, 'c' : 30}
D2 = D1.copy()
id(D1)
2339489218496
id(D2)
2339489218304
D1 == D2
True
D1 is D2
False
S1 = {100, 200, 300}
S2 = S1.copy()
S1 == S2
True
S1 is S2
False
b1 = False
b1.copy()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b1.copy()
AttributeError: 'bool' object has no attribute 'copy'
n = 100
n.copy()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    n.copy()
AttributeError: 'int' object has no attribute 'copy'
f_num = 1.1
f_num.copy()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    f_num.copy()
AttributeError: 'float' object has no attribute 'copy'
s1 = "Hello
SyntaxError: unterminated string literal (detected at line 1)
s1 = "Hello"
s1.copy()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s1.copy()
AttributeError: 'str' object has no attribute 'copy'
T = (100, 200, 300)
T.copy()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    T.copy()
AttributeError: 'tuple' object has no attribute 'copy'
# ARGUMENT -> COPY FUNCTION IS A SHALLOW VERSION OF DEEP COPYING
L1 = [10, 20, 30, 40]
L2 = L1.copy()
id(L1)
2339488325696
id(L2)
2339489381952
L1 is L2
False
L1 == L2
True
for x in L1:
    print(x, id(x))

    
10 140734957069720
20 140734957070040
30 140734957070360
40 140734957070680
for x in L2:
    print(x, id(x))

    
10 140734957069720
20 140734957070040
30 140734957070360
40 140734957070680
# as 10, 20, 30, 40 all are immutable objects, them being shared across L1 & L2 is NOT PARTICULARLY PROBLEMETIC
# IF A LIST CONTAINS A MUTABLE OBJECT INSIDE IT THEN IT BECOMES PROBLEMETIC
L1 = [10, 20, 30, [100, 200, 300], 40]
L2 = L1.copy()
id(L1)
2339489167936
id(L2)
2339488325696
L1 is L2
False
L1 == L2
True
L1[3]
[100, 200, 300]
L2[3]
[100, 200, 300]
id(L1[3])
2339444617088
id(L2[3])
2339444617088
L1[3].append(400)
L2
[10, 20, 30, [100, 200, 300, 400], 40]
>>> import copy
>>> L1 = [10, 20, 30, [100, 200, 300], 40]
>>> L2 = copy.deepcopy(L1)
>>> id(L1)
2339489410304
>>> id(L2)
2339489167488
>>> id(L1[0])
140734957069720
>>> id(L2[0])
140734957069720
>>> id(L1[1])
140734957070040
>>> id(L2[1])
140734957070040
>>> id(L1[2])
140734957070360
>>> id(L2[2])
140734957070360
>>> id(L1[3])
2339489409344
>>> id(L2[3])
2339489160320
>>> L1[3].append(400)
>>> L2
[10, 20, 30, [100, 200, 300], 40]
>>> L1
[10, 20, 30, [100, 200, 300, 400], 40]
>>> L1[3]
[100, 200, 300, 400]
>>> L2[3]
[100, 200, 300]
>>> id(L1[3][0])
140734957072600
>>> id(L2[3][0])
140734957072600
