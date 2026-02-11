Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> (lambda n : n ** 2)
<function <lambda> at 0x0000029561E359B0>
>>> def func(n):
...     return n ** 2
... 
>>> func
<function func at 0x0000029561E35A60>
>>> #---------------------------------------------------
>>> 
>>> result = (lambda n : if n % 2 == 0: print(n, 'is an even number'))(100)
SyntaxError: invalid syntax
>>> #-----------------------------------------------------
>>> 
>>> def myFunc(a, b, c=100):
...     print(a, b, c)
... 
...     
>>> myFunc(10, 20)
10 20 100
>>> myFunc(10, 20, c=200)
10 20 200

>>> (lambda a, b, c=100 : print(a, b, c))(10, 20)
10 20 100
>>> (lambda a, b, c=100 : print(a, b, c))(10, 20, c=200)
10 20 200
>>> #-------------------------------------------------------
>>> 
>>> def myFunc(*args):
...     print(args)
... 
...     
>>> myFunc()
()
myFunc(100)
(100,)
myFunc(100, 200)
(100, 200)
myFunc(100, 200, 300)
(100, 200, 300)

(lambda *args : print(args))()
()
(lambda *args : print(args))(100)
(100,)
(lambda *args : print(args))(100, 200)
(100, 200)
(lambda *args : print(args))(100, 200, 300)
(100, 200, 300)
#----------------------------------------------------------

a = 1.1
b = 2.2
c = 3.3
(lambda x, y, z : (a*x + b&y + c*z)*3.0)(10, 20, 30)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    (lambda x, y, z : (a*x + b&y + c*z)*3.0)(10, 20, 30)
  File "<pyshell#36>", line 1, in <lambda>
    (lambda x, y, z : (a*x + b&y + c*z)*3.0)(10, 20, 30)
TypeError: unsupported operand type(s) for &: 'float' and 'float'
(lambda x, y, z : (a*x + b*y + c*z)*3.0)(10, 20, 30)
462.0
(1.1 * 10 + 2.2 * 20 + 3.3 * 30) * 3.0
462.0
#---------------------------------------------------------
