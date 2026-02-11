Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Basic list operations
# Creating an empty list
L1 = []
print(L1)
[]
id(L1)
2270988621824
type(L1)
<class 'list'>
type(L1)
<class 'list'>
len(L1)
0
# Creating a list with some data
L2 = [10, 20, 30, 40, 50]
print(L2)
[10, 20, 30, 40, 50]
t
type(L2)
<class 'list'>
id(L2)
2270988620032
len(L2)
5
# Creating a list with different data element at each index
L3 = [True, 10, 3.14, "Hello"]
print(L3)
[True, 10, 3.14, 'Hello']
type(L3)
<class 'list'>
id(L3)
2270988538432
len(L3)
4
L3[0]
True
>>> type(L3[0])
<class 'bool'>
>>> L3[1]
10
>>> type(L3[1])
<class 'int'>
>>> L3[2]
3.14
>>> type(L3[2])
<class 'float'>
>>> L3[3]
'Hello'
>>> type(L3[3])
<class 'str'>
>>> # How to insert new data into the list object
>>> # Create an empty list
>>> L = []
>>> print(L)
[]
>>> len(L)
0
>>> L.append(10) # Function applied on the object must be defined in the class of the object.
>>> # Object on which function is applied is passed as the first actual parameter
>>> # L.append(10) == list.append(L, 10)
>>> print(L)
[10]
>>> # Problem: Let L be the following list
>>> # L = [True, 10, False, 20]
>>> # Visit list L element by element and print them using while loop
>>> i = 0
>>> while i < len(L):
...     print(i, L[i])
    i = i + 1

    
0 10
# We did not initialize L to [True, 10, False, 20]. The varaible L was naming a list object containing value 10
# That explains the above output
# Lets solve the problem again. This time we will start with initializing the list
L = [True, 10, False, 20]
i = 0
while i < len(L):
    print(i, L[i])
    i = i + 1

    
0 True
1 10
2 False
3 20
