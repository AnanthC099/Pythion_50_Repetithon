'''
@author: Yogeshwar Shukla

@date: 19th November 2025 

@goal:  To write a simple text file copying utility. 
        This program accepts one source file and 
        a destination file on command line and copies 
        source file into the destination file. 

        The source file must exist. Destination file 
        may or may not exist 

@commandline: 
        # python cp2.py source_file_path destination_file_path
'''


import sys 


def copy_file(source_file_path:str, destination_file_path:str) -> bool:
    if type(source_file_path) is not str or type(destination_file_path) is not str: 
        return False 

    source_file_handle = open(source_file_path, 'r')
    destination_file_handle = open(destination_file_path, 'w')

    for line in source_file_handle: 
        print(line, end='', file=destination_file_handle)

    source_file_handle.close() 
    destination_file_handle.close() 
    
    return True 


def main(argc:int, argv:list[str]) -> None: 
    if argc != 3: 
        print('UsageError:Correct Usage:', argv[0], 'SourceFilePath DestinationFilePath')
        sys.exit(-1)
    
    source_file_path = argv[1] 
    destination_file_path = argv[2]

    copy_status = copy_file(source_file_path, destination_file_path)
    if copy_status is True: 
        print('File copied successfully')
        exit_status = 0 
    else: 
        print('Error in copying file')
        exit_status = -1

    sys.exit(exit_status) 
    

main(len(sys.argv), sys.argv)
