Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Basic boolean operators
b1 = False
b2 = True
type(b1)
<class 'bool'>
type(b2)
<class 'bool'>
int("1")
1
int(1.0)
1
int(True)
1
int("0")
0
int(0.0)
0
int(False)
0
#--------------------
# Not operator
print('b1:', b1)
b1: False
c = not b1
print('b1:', b1)
b1: False
print('c:', c)
c: True
print('b2:', b2)
b2: True
c = not b2
print('b2:', b2)
b2: True
print('c:', c)
c: False
#-------------------
# And operator
print('b1:', b1, 'b2:', b2)
b1: False b2: True
c = b1 and b2
print('c:', c)
c: False
c = b1 and b1
>>> print('c:', c)
c: False
>>> c = b2 and b1
>>> print('c:', c)
c: False
>>> c = b2 and b2
>>> print('c:', c)
c: True
>>> #---------------------
>>> # Or opeartor
>>> print('b1:', b1, 'b2:', b2)
b1: False b2: True
>>> c = b1 or b1
>>> print('c:', c)
c: False
>>> c = b1 or b2
>>> print('c:', c)
c: True
>>> c = b2 or b1
>>> print('c:', c)
c: True
>>> 
>>> c = b2 or b2
>>> print('c:', c)
c: True
