'''
@author:        Yogeshwar Shukla 

@date:          20th November 2025 

@version:       1.0 

@goal:          This file implements a simplified version of 'wc' command in the 
                core-utils package of Linux OS. 

                wc1.py accepts a file path on command-line and counts number of 
                lines, words, characters in it and prints them on the console. 

@commandline:   # python wc1.py file_path 
'''


import sys 


def get_word_count(s:str) -> int: 
    if type(s) is not str: 
        return -1 
    
    if len(s) == 0: 
        return 0 
    
    IN = 1 
    OUT = 2 
    currentState = OUT 
    word_count = 0 

    for c in s: 
        if currentState is OUT and not c.isspace(): 
            word_count += 1 
            currentState = IN 
        elif currentState is IN and c.isspace(): 
            currentState = OUT 

    return word_count 


def main(argc:int, argv:list[str]) -> None: 
    if argc != 2: 
        print('UsageError:Correct usage is:', argv[0], 'file_path')
        sys.exit(-1)

    
    character_count = 0 
    word_count = 0 
    line_count = 0 
    
    f_handle = open(argv[1], 'r')
    for line in f_handle: 
        line_count = line_count + 1 
        word_count = word_count + get_word_count(line)
        character_count = character_count + len(line)
    f_handle.close() 

    print("In file:", argv[1])
    print('Character Count:', character_count) 
    print('Word Count:', word_count) 
    print('Line Count:', line_count)

    sys.exit(0) 


main(len(sys.argv), sys.argv)