num = 100 # num is a global variable 

def func1():
    print('Inside func1():', num)  # I am accessing global variable num

func1() 
print('func1() DEMO END')
#-------------------------------------------------------

f_num = 1.1     # f_num is a global variable 

def func2():
    global f_num
    print('Entered func2()') 
    f_num = 2.2
    print('Leaving func2()') 

print('Printing f_num before calling func2():', f_num)
func2()
print('Printing f_num after calling func2():', f_num)
    
#-------------------------------------------------------
