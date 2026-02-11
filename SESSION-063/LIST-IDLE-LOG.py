Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # String data type in depth
>>> # Methods of creation
>>> # Singly quoted string
>>> s1 = 'Hello,World'
>>> # Doubly quoted string
>>> s2 = "Hello,World"
>>> # Singly quoted string can contain double quote as a data
>>> s = 'This is "supposedly" a time for study'
>>> print(s)
This is "supposedly" a time for study
>>> # Doubly quoted string can contain single quote as a data
>>> s = "This is John's room"
>>> print(s)
This is John's room
>>> # You will require backlash (escape) in order to put " inside doubly quoted string
>>> # You will require backslash (escape) in order to put ' inside singly quoted string
>>> s = 'This is John\'s room'
>>> print(s)
This is John's room
>>> s = "This is \"Supposedly\" a time for study"
>>> print(s)
This is "Supposedly" a time for study
>>> s1 = "Hello\nWorld"
s
>>> s2 = 'Hello\nWorld'
>>> print(s1)
Hello
World
>>> print(s2)
Hello
World
>>> # Third way of creating string (raw string) -> raw string is not a new data type
>>> s = r"Hello\nWorld"
>>> print(s)
Hello\nWorld
s = r'Hello\nWorld'
print(s)
Hello\nWorld
type(s)
<class 'str'>
path = 'C:\new folder\abc.txt'
print(path)
C:
ew folderbc.txt
s = '\'
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
s = '\\'
print(s)
\
path = "C:\\new folder\\abc.txt"
print(path)
C:\new folder\abc.txt
# You can use raw string here!
path = r'C:\new folder\abc.txt'
print(path)
C:\new folder\abc.txt
path = r'
SyntaxError: unterminated string literal (detected at line 1)
# Fourth way of creating string
# Triple quoted string
s = "Hello
SyntaxError: unterminated string literal (detected at line 1)
s = '''Dear sir,
I will not be able to attend today's session due to semester examination.
Yours truly,
XYZ
'''
print(s)
Dear sir,
I will not be able to attend today's session due to semester examination.
Yours truly,
XYZ

s = '''This is a doubly quoted string " this is a singly qutoed string ' both are present '''
print(s)
This is a doubly quoted string " this is a singly qutoed string ' both are present 
# Fifth way of creating string
# Constructor approach
# If you want to create a string representation of object of any type
# You can provide that object as an initialization data for string constructor
L = [10, 20, 30, 40]
print(L)
[10, 20, 30, 40]
str(L)
'[10, 20, 30, 40]'
s = "Hello"
print(s)
Hello
s
'Hello'
s = input("Enter an integer:")
Enter an integer:456
# Sixth way : Format string
roll_number = 100
salary = 5000.5
print("My name roll number is", roll_number, "and my salary is", salary)
My name roll number is 100 and my salary is 5000.5
print("My roll number is %d and my salary is %f" % (roll_number, salary) )
My roll number is 100 and my salary is 5000.500000
L = [1, 6, 10]
print("My team is", L)
My team is [1, 6, 10]
s = 'My team is {L}'
print(s)
My team is {L}
s = f'My team is {L}'
print(s)
My team is [1, 6, 10]
print(f'My roll number is {roll_number} and my salary is {salary}')
My roll number is 100 and my salary is 5000.5
#---------------------------------------------------------------------------
# PART 2: Operators that are compatible with string object
# Concat
s1 = "Hello"
s
s2 = "World"
s3 = s1 + s2
print(s1)
Hello
print(s2)
World
print(s3)
HelloWorld
# Multiplication by integer
s = "Hello"
s1 = s * 5
print(s)
Hello
print(s1)
HelloHelloHelloHelloHello
line = '-' * 80
print(line)
--------------------------------------------------------------------------------
# Index, Range, Slice
s = "Hello"
s_reversed = s[::-1]
print(s)
Hello
print(s_reversed)
olleH
s [ 0 : 12 : -1]
''
s [ 12 : 0 : -1]
'olle'
len(s)
5
s [5 : 0 : -1]
'olle'
s[::-1]
'olleH'
# membership testing operator
s = "aabbbbaabbbbbbbaa"
'aa' in s
True
'xy' in s
False
'bbb' in s
True
#---------------------------------------------
# PART 3 : Built in functions that are compatible with string object
s = "Hello"
print(s)
Hello
t
type(s)
<class 'str'>
len(s)
5
id(s)
3076200265120
#-----------------------------------------------------------
# PART 4: Class methods
s = "xyzAAxyzAAxyzAA"
s.index('z')
2
s.index('z', 3)
7
s.index('z', 8)
12
s.index('AA')
3
s.index('AA', 4)
8
s.index('
        
SyntaxError: unterminated string literal (detected at line 1)
s.index('AA', 9)
        
13
s.count('z')
        
3
s.count('AA')
        
3
s.count('u')
        
0
type('x')
        
<class 'str'>
type('y')
        
<class 'str'>
type('z')
        
<class 'str'>
type('xyz')
        
<class 'str'>
#----------------------------------------------------
        
# strip(), rstrip(), lstrip(
        
s = "\t\tn = 10\n"
        
s1 = s.strip()
        
s
        
'\t\tn = 10\n'
s1
        
'n = 10'
s2 = s.rstrip()
        
s
        
'\t\tn = 10\n'
s2
        
'\t\tn = 10'
s3 = s.lstrip()
        
s
        
'\t\tn = 10\n'
s3
        
'n = 10\n'
#---------------------------------------------------
        
# split() and rsplit()
        
s = 'abc:pqr:xyz:lmn'
        
L = s.split(':')
        
L
        
['abc', 'pqr', 'xyz', 'lmn']
s
        
'abc:pqr:xyz:lmn'
s = 'abc:pqr:xyz:lmn:uvw:rst:vbn:mno'
        
s.split(':')
        
['abc', 'pqr', 'xyz', 'lmn', 'uvw', 'rst', 'vbn', 'mno']
s.rsplit(':')
        
['abc', 'pqr', 'xyz', 'lmn', 'uvw', 'rst', 'vbn', 'mno']
s.split(':')
        
['abc', 'pqr', 'xyz', 'lmn', 'uvw', 'rst', 'vbn', 'mno']
s.split(':', maxsplit=2)
        
['abc', 'pqr', 'xyz:lmn:uvw:rst:vbn:mno']
s.rsplit(':', maxsplit=2)
        
['abc:pqr:xyz:lmn:uvw:rst', 'vbn', 'mno']
