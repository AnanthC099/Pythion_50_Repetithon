# LIST-IDLE-LOG.py
# Converted from IDLE session log to executable Python script
# Topic: String data type in depth

# ---- Methods of creating strings ----

# Singly quoted string
s1 = 'Hello,World'
# Doubly quoted string
s2 = "Hello,World"

# Singly quoted string can contain double quote as data
s = 'This is "supposedly" a time for study'
print(s)

# Doubly quoted string can contain single quote as data
s = "This is John's room"
print(s)

# Backslash (escape) to put ' inside singly quoted string
s = 'This is John\'s room'
print(s)

# Backslash (escape) to put " inside doubly quoted string
s = "This is \"Supposedly\" a time for study"
print(s)

# Newline escape
s1 = "Hello\nWorld"
s2 = 'Hello\nWorld'
print(s1)
print(s2)

# Third way: raw string (raw string is not a new data type)
s = r"Hello\nWorld"
print("raw string:", s)
s = r'Hello\nWorld'
print("raw string:", s)
print("type(s):", type(s))

# Demonstrating path issues with backslash
path = "C:\\new folder\\abc.txt"
print("escaped path:", path)

# Using raw string for paths
path = r'C:\new folder\abc.txt'
print("raw path:", path)

# Fourth way: Triple quoted string (multi-line)
s = '''Dear sir,
I will not be able to attend today's session due to semester examination.
Yours truly,
XYZ
'''
print(s)

s = '''This is a doubly quoted string " this is a singly quoted string ' both are present '''
print(s)

# Fifth way: Constructor approach
L = [10, 20, 30, 40]
print("L:", L)
print("str(L):", str(L))

s = "Hello"
print("s:", s)
print("repr(s):", repr(s))

# Sixth way: Format string
roll_number = 100
salary = 5000.5
print("My roll number is", roll_number, "and my salary is", salary)
print("My roll number is %d and my salary is %f" % (roll_number, salary))
L = [1, 6, 10]
print("My team is", L)
s = 'My team is {L}'
print("without f-string:", s)
s = f'My team is {L}'
print("with f-string:", s)
print(f'My roll number is {roll_number} and my salary is {salary}')

# ---- PART 2: Operators compatible with string object ----
print("\n--- Operators compatible with string ---")

# Concat
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print("s1:", s1)
print("s2:", s2)
print("s1 + s2:", s3)

# Multiplication by integer
s = "Hello"
s1 = s * 5
print("s * 5:", s1)
line = '-' * 80
print(line)

# Index, Range, Slice
s = "Hello"
s_reversed = s[::-1]
print("s:", s)
print("s[::-1]:", s_reversed)
print("s[0:12:-1]:", s[0:12:-1])
print("s[12:0:-1]:", s[12:0:-1])
print("len(s):", len(s))
print("s[5:0:-1]:", s[5:0:-1])
print("s[::-1]:", s[::-1])

# Membership testing operator
s = "aabbbbaabbbbbbbaa"
print("\n'aa' in s:", 'aa' in s)
print("'xy' in s:", 'xy' in s)
print("'bbb' in s:", 'bbb' in s)

# ---- PART 3: Built-in functions compatible with string object ----
print("\n--- Built-in functions ---")
s = "Hello"
print("s:", s)
print("type(s):", type(s))
print("len(s):", len(s))
print("id(s):", id(s))

# ---- PART 4: Class methods ----
print("\n--- Class methods ---")

# index() and count()
s = "xyzAAxyzAAxyzAA"
print("s:", s)
print("s.index('z'):", s.index('z'))
print("s.index('z', 3):", s.index('z', 3))
print("s.index('z', 8):", s.index('z', 8))
print("s.index('AA'):", s.index('AA'))
print("s.index('AA', 4):", s.index('AA', 4))
print("s.index('AA', 9):", s.index('AA', 9))
print("s.count('z'):", s.count('z'))
print("s.count('AA'):", s.count('AA'))
print("s.count('u'):", s.count('u'))

# strip(), rstrip(), lstrip()
print("\n--- strip(), rstrip(), lstrip() ---")
s = "\t\tn = 10\n"
s1 = s.strip()
print("s:", repr(s))
print("s.strip():", repr(s1))
s2 = s.rstrip()
print("s.rstrip():", repr(s2))
s3 = s.lstrip()
print("s.lstrip():", repr(s3))

# split() and rsplit()
print("\n--- split() and rsplit() ---")
s = 'abc:pqr:xyz:lmn'
L = s.split(':')
print("s.split(':'):", L)
print("s:", s)

s = 'abc:pqr:xyz:lmn:uvw:rst:vbn:mno'
print("s.split(':'):", s.split(':'))
print("s.rsplit(':'):", s.rsplit(':'))
print("s.split(':', maxsplit=2):", s.split(':', maxsplit=2))
print("s.rsplit(':', maxsplit=2):", s.rsplit(':', maxsplit=2))
