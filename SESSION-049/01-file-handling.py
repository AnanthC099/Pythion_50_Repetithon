# Task: create a new file abc.txt in the current directory
# Python supports high level file handling as a part of language implementation 

file_name = 'abc.txt'

f_handle = open(file_name, 'w')

# _io.TextIOWrapper
print('type(f_handle):', type(f_handle))
print('TOKEN RETURNED FROM OS:', f_handle.fileno()) # 3 

f_handle.close() 


