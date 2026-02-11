Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Function with 0 or no formal parameter
def TestFunction():
    print('This is a TestFunction() which does nothing apart from printing this msg')

    
TestFunction()
This is a TestFunction() which does nothing apart from printing this msg
TestFunction()
This is a TestFunction() which does nothing apart from printing this msg
TestFunction()
This is a TestFunction() which does nothing apart from printing this msg
#------------------------------------------------------------------------------
# Function with 1 formal parameter
def TestFunction(param_1):
    print('Value of param_1:', param_1)
    print('Type of param_1:', type(param_1))
    print('Id if param_1:', id(param_1))

    
TestFunction(1500)
Value of param_1: 1500
Type of param_1: <class 'int'>
Id if param_1: 2180940280752
TestFunction(1.1)
Value of param_1: 1.1
Type of param_1: <class 'float'>
Id if param_1: 2180940273328
TestFunction('Yogeshwar')
Value of param_1: Yogeshwar
Type of param_1: <class 'str'>
Id if param_1: 2180946504496
TestFunction(1500)
Value of param_1: 1500
Type of param_1: <class 'int'>
Id if param_1: 2180940280848
#---------------------------------------
def TestFunction(x, y):
    print('Value of x:', x)
    print('Type of x:', type(x))
    print('id of x:', id(x))
    print('Value of y:', y)
    print('Type of y:', type(y))
    print('id of y:', id(y))

    
TestFunction(100, 200)
Value of x: 100
Type of x: <class 'int'>
id of x: 140730589783576
Value of y: 200
Type of y: <class 'int'>
id of y: 140730589786776
>>> TestFunction(100, 1.1)
Value of x: 100
Type of x: <class 'int'>
id of x: 140730589783576
Value of y: 1.1
Type of y: <class 'float'>
id of y: 2180940278096
>>> TestFunction(100, 'Hello')
Value of x: 100
Type of x: <class 'int'>
id of x: 140730589783576
Value of y: Hello
Type of y: <class 'str'>
id of y: 2180946468976
>>> TestFunction('Hello', 'World')
Value of x: Hello
Type of x: <class 'str'>
id of x: 2180946468976
Value of y: World
Type of y: <class 'str'>
id of y: 2180946465904
