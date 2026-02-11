'''
@author:        Yogeshwar Shukla 
@date:          20th November 2025 
@version:       1.0 
@goal:          To implement word count algorithm. 
                The algorithm accepts string as 
                input parameter and returns number 
                of words in the given string. 

                Word is defined as follows: 
                First non-white-space character to 
                last non-white-space charater. 
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


def main(): 
    str_for_word_count = input("Enter a string for word counting:")
    w_count = get_word_count(str_for_word_count)
    print('Words in the given strings are:', w_count)

    sys.exit(0) 


main()