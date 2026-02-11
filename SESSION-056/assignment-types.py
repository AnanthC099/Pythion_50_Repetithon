Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> (a, b, c) = (10, 20, 30) # tuple positional assignment
>>> a
10
>>> b
20
 
>>> c
30
>>> [p, q, r] = [1.1, 2.2, 3.3]
>>> p
1.1
>>> q
2.2
>>> r
3.3
>>> u, v, w = True, False, True
>>> u
True
>>> v
False
>>> w
True
>>> u, v, w = 10, 20, 30, 40
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    u, v, w = 10, 20, 30, 40
ValueError: too many values to unpack (expected 3, got 4)
>>> u, v = 10, 20, 30
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    u, v = 10, 20, 30
ValueError: too many values to unpack (expected 2, got 3)
>>> u, v, w, s = 10, 20
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    u, v, w, s = 10, 20
ValueError: not enough values to unpack (expected 4, got 2)
