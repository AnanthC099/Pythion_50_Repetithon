'''
@author:        Yogeshwar Shukla
@date:          19th November 2025
@version:       0.1 
@goal:          Goal of this application is to accept one or more 
                source files and one destination file from command line 
                and copy all source file in the destination file in the 
                order they were mentioned on the command line 
@commandline:   # python ncp.py src_file_1.txt source_file_2.txt   ...     source_file_n.txt destination_file.txt
@validation:    ncp command should receive at least one source and one destination file. 
                All source files must exist. Destination file may or may not exist 
@example:       # python ncpy.py abc.txt pqr.txt lmn.txt MASTER.txt 
                source files: abc.txt, pqr.txt and lmn.txt 
                These must be present 

                Destination file: MASTER.txt 
                This may or may not be present. 

                Master.txt will contain the contents of 
                abc.txt followed by that of pqr.txt, and followed 
                by that of lmn.txt. 
'''


import sys


def copy_file(source_file_path:str, destination_file_path:str) -> bool: 
    if type(source_file_path) is not str or type(destination_file_path) is not str: 
        return False 
    
    source_file_handle = open(source_file_path, 'r') 
    destination_file_handle = open(destination_file_path, 'a')

    for line in source_file_handle: 
        print(line, end='', file=destination_file_handle)

    source_file_handle.close() 
    destination_file_handle.close() 
    return True 


def main(argc:int, argv:list[str]) -> None: 
    if argc < 3: 
        print('UsageError:Correct usage is:', argv[0], 'src_file_1 src_file_2 ... src_file_n destination_file')
        sys.exit(-1)

    exit_status = 0 
    i = 1 
    while i <= argc-2: 
        return_status = copy_file(argv[i], argv[argc-1])
        if return_status is False: 
            exit_status = -1 
            break 
        i = i + 1 
    
    sys.exit(exit_status) 


main(len(sys.argv), sys.argv)