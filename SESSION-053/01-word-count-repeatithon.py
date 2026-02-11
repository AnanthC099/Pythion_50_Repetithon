# 1 
def get_word_count(s:str) -> int: 
    if type(s) is not str: 
        return -1 
    if len(s) == 0: 
        return (0) 
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

# 1 
def get_word_count(s:str) -> int: 
    if type(s) is not str: 
        return -1 
    if len(s) is 0: 
        return 0 
    IN, OUT = 1, 2 
    currentState = OUT 
    w_cnt = 0 
    for c in s: 
        if currentState is OUT and c.isspace() is False: 
            currentState = IN 
            w_cnt = w_cnt + 1 
        elif currentState is IN and c.isspace() is True: 
            currentState = IN 
    return w_cnt 

# 2 
def get_word_count(s:str) -> int: 
    if type(s) is not str: 
        return -1 
    if len(s) == 0: 
        return 0 
    IN, OUT = 1, 2 
    currentState = OUT 
    w_cnt = 0 
    for c in s: 
        if currentState is OUT and c.isspace() is False: 
            currentState = IN 
            w_cnt = w_cnt + 1 
        elif currentstate is IN and c.isspace() is True: 
            currentState = OUT 
    return w_cnt 

# 3 
def get_word_count(s:str) -> int: 
    if type(s) != str: 
        return -1 
    if len(s) == 0: 
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

# 4 
def get_word_count(s:str) -> int: 
    if type(s) != str: 
        return -1 
    if len(s) == 0: 
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

# 5 
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
