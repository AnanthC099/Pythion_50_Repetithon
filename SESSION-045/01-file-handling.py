'''
@author: Yogeshwar Shukla 
@goal: To demonstrate basic file handling operations. 
How to 
a) Open File 
b) Read File 
c) Write File 
d) Close File
? 
Using Python Functions. 
'''

# Step 1: Create a text file named abc.txt 
f_handle = open('abc.txt', 'w') 

# For understanding - Begin 
print('type(f_handle):', type(f_handle))
# For understanding - End 

# Step 2: Write some content on the file 
print('This is a first line in the file', file=f_handle)
print('CoreCode Programming Academy', file=f_handle)
L = [True, 10, 3.14, "Hello"]
for x in L: 
    print(x, file=f_handle)
print('This is the last line in the file', file=f_handle)

# Step 3: Close the file 
f_handle.close() 

# Step 4: Re-open the file in read mode 
f_handle = open('abc.txt', 'r')

# Step 5: Read the file line by line and display each line on the console 
for line in f_handle: 
    print(line, end='')

# Step 6: Close the file 
f_handle.close() 

