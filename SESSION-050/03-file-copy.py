'''
@author: Yogeshwar Shukla 
@goal:  The current directory contains a file named abc.txt having 
        8 lines in it. This file is created by different Python application. 
        Our aim is to clone this file. Our application should create a file 
        named lmn.txt in the current directory and should copy all lines from 
        abc.txt and paste them in lmn.txt 
'''

# Create two variables holding paths of source and destination files 
source_file = 'abc.txt'
destination_file = 'lmn.txt'

# Open source file in read mode because the source file must be present 
# at the time of opening. Also, we do not need to modify the contents of 
# source file and therefore, 'read' is the most appropriate mode for it. 

# Open destination file in the write mode. The desintation file may or may not 
# be present in the current directory. 
# Because the mode is 'write' mode, it will be created if not present.
# If it is present already then its existing contents are deleted and 
# empty version of file is opened. Both of these behaviours are suitable 
# to us. 

source_file_handle = open(source_file, "r")
destination_file_handle = open(destination_file, "w")

# Read source file line by line and write each line in the 
# destination file. To avoid extra space between two lines
# we ask print() not to put its default end of line which is '\n' 
# by overriding its default end of line by keeping 'end' parameter to ''
for line in source_file_handle: 
    print(line, end='', file=destination_file_handle)
# At this point all lines in the source file have been copied into destination 
# file 

# Close source and desteination files. 
# Closing the destination file ensures any pending data in main memory 
# is synced with its on disk copy
source_file_handle.close() 
destination_file_handle.close() 
