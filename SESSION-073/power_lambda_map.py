with open('test.txt', 'r') as f_handle: 
    for capitalized_line in map(lambda line: line.upper(), f_handle): print(capitalized_line, end='')
# test.txt is closed here
