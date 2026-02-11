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
# <other package imports> 


def main(argc:int, argv:list[str]) -> None: 
    
    sys.exit(0) 


main(len(sys.argv), sys.argv)