'''
@author:        Yogeshwar Shukla 

@date:          20th November 2025 

@version:       2.0 

@goal:          This file implements 'wc' command in the core-utils package of Linux OS. 

                wc2.py accepts a file path(s) on command-line and counts number of 
                lines, words, characters in each of them and prints them on the console. 
                If more than one file is provided then cumulative stats are also printed. 

@commandline:   # python wc1.py file_path(s)
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
    if argc < 2: 
        print('UsageError:Correct usage is:', argv[0], 'file_path(s)')
        sys.exit(-1)

    
    total_line_count, total_word_count, total_character_count = 0, 0, 0 

    i = 1 
    while i <= (argc - 1): 
        current_line_count, current_word_count, current_character_count = 0, 0, 0 
        f_handle = open(argv[i], 'r')
        for line in f_handle: 
            current_line_count = current_line_count + 1 
            current_word_count = current_word_count + get_word_count(line)
            current_character_count = current_character_count + len(line)
        f_handle.close() 

        print(current_line_count, current_word_count, current_character_count, argv[i], sep='\t')
        total_line_count = total_line_count + current_line_count 
        total_word_count = total_word_count + current_word_count 
        total_character_count = total_character_count + current_character_count

        i = i + 1 

    if argc > 2: 
        print(total_line_count, total_word_count, total_character_count, "total", sep='\t')


    sys.exit(0) 


main(len(sys.argv), sys.argv)