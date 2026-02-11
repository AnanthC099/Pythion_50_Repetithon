with open('test.txt', 'r') as f_handle: 
    for capitalized_line in map(lambda line: line.upper(), f_handle): print(capitalized_line, end='')
# abc.txt is closed here 
