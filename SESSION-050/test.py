f_handle = open('test.txt', 'r')

for line in f_handle: 
    print(line, end='')
    print(id(line))
    print('-------------')

f_handle.close()