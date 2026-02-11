import sys 

if len(sys.argv) != 3: 
    print('UsageError:Correct Usage is:', sys.argv[0], 'SourcePath DestinationPath')
    sys.exit(-1)

source_file_path = sys.argv[1]
destination_file_path = sys.argv[2]

source_file_handle = open(source_file_path, 'r')
destination_file_handle = open(destination_file_path, 'w')

for line in source_file_handle: 
    print(line, end='', file=destination_file_handle)

source_file_handle.close() 
destination_file_handle.close()