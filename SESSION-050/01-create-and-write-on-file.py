# Create new file abc.txt
f_handle = open('abc.txt', 'w')

# Write some content on the file 
print("The is first line", file=f_handle)
print("Hello,World", file=f_handle)

L = [10, 20, 30, 40, 50]
for x in L: 
    print(x, file=f_handle) 

print('This is the last line', file=f_handle)

# Release the file 
f_handle.close() 

# Reopen the file in the read mode 
f_handle = open('abc.txt', 'r')

# read and display file line by line 
for line in f_handle: 
    print(line, end='')

# Release the file 
f_handle.close() 

'''
print() 
high level fwrite() 
os.write() 
PYTHON/C INTEGRATION 
write(fileno, buffer, buffersize)  # linux / MAC OS 
WriteFile() # Windows 

VFS -> file system driver 

Linux: ext4_write() | btrfs_write() 
Windows: nfts_write() 

Generic Block IO layer 
I/O request Queue -> request register 

Physical media driver 

HARDWARE WRITE 
'''

