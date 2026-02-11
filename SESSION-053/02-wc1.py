def get_word_count(s:str) -> int: 
    if type(s) is not str: 
        return -1 
    if len(s) == 0
        return 0 
    IN, OUT = 1, 2 
    currentState = OUT 
    w_cnt = 0 
    for c in s: 
        if currentState is OUT and c.isspace() is False: 
            currentState = IN 
            w_cnt = w_cnt + 1 
        elif currentState is IN and c.isspace() is True: 
            currentState = OUT 
    return w_cnt 
#-----------------------------------------------------------------------
file_name = 'abc.txt'
line_count, word_count, character_count = 0, 0, 0 
f_handle = open(file_name, 'r')
for line in f_handle: 
    line_count = line_count + 1 
    word_count = word_count + get_word_count(line)
    character_count = character_count + len(line)
f_handle.close() 
print(line_count, word_count, character_count, file_name, sep='\t')
#-----------------------------------------------------------------------
# 1 
file_name = 'pqr.txt'
line_count, word_count, character_count = 0, 0, 0 
f_handle = open(file_name, 'r')
for line in f_handle: 
    line_count = line_count + 1 
    word_count = word_count + get_word_count(line)
    character_count = character_count + len(line)
f_handle.close() 
print(line_count, word_count, character_count, file_name, sep='\t')
#-----------------------------------------------------------------------
# 2 
file_name = 'abc.txt'
line_count, word_count, character_count = 0, 0, 0 
f_handle = open(file_name, 'r')
for line in f_handle: 
    line_count = line_count + 1 
    word_count = word_count + get_word_count(line)
    character_count = character_count  + len(line)
f_handle.close() 
print(line_count, word_count, character_count, file_name, sep='\t')
#-----------------------------------------------------------------------
#3 
file_name = 'abc.txt'
line_count, word_count, character_count = 0, 0, 0 
f_handle = open(file_name, 'r')
for line in f_handle: 
    line_count = line_count + 1 
    word_count = word_count + get_word_count(line)
    character_count = character_count + len(line)
f_handle.close() 
print(line_count, word_count, character_count, file_name, sep='\t')
#-----------------------------------------------------------------------
#4 
file_name = 'abc.txt'
line_count, word_count, character_count = 0, 0, 0 
f_handle = open(file_name, 'r')
for line in f_handle: 
    line_count = line_count + 1 
    word_count = word_count + get_word_count(line)
    character_count = character_count + len(line)
f_handle.close() 
print(line_count, word_count, character_count, file_name, sep='\t')
#-----------------------------------------------------------------------
#5 
file_name = 'abc.txt'
line_count, word_count, character_count = 0, 0, 0 
f_handle = open(file_name, 'r')
for line in f_handle: 
    line_count = line_count + 1 
    word_count = word_count + get_word_count(line)
    character_count = character_count + len(line)
f_handle.close() 
print(line_count, word_count, character_count, file_name, sep='\t')
#-----------------------------------------------------------------------

