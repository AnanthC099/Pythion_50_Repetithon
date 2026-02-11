Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = 'hello'
print(s)
hello
type(s)
<class 'str'>
s1 = s.upper()
print(s)
hello
print(s1)
HELLO
#--------------------------
u = 'PYTHON'
print(u)
PYTHON
t
type(u)
<class 'str'>
u1 = u.lower()
print(u)
PYTHON
print(u1)
python
#-------------------------
>>> s = 'CoreCode:Programming:Academy'
>>> L = s.split(':')
>>> print(s)
CoreCode:Programming:Academy
>>> print(L)
['CoreCode', 'Programming', 'Academy']
>>> #-------------------------------------
>>> s = 'hello'
>>> s1 = s.upper()
>>> print(s1)
HELLO
>>> type(s)
<class 'str'>
>>> u = 'yogeshwar'
>>> print(u)
yogeshwar
>>> type(u)
<class 'str'>
>>> # u1 = u.upper()
>>> u1 = str.upper(u)
>>> print(u1)
YOGESHWAR
>>> v = 'Yogeshwar:Vidyadhar:Shukla'
>>> # L = v.split(':')
>>> L = str.split(v, ':')
>>> L
['Yogeshwar', 'Vidyadhar', 'Shukla']
