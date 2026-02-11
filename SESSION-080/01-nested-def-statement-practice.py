# Two level nesting - already covered 
# Predict the output 
def f1(n): 
    print(f'n:{n}')
    def f2(x, y): 
        print(f'x:{x}, y:{y}')
    z = 100 
    print(f'z:{z}')
    f2(True, False) 
f1(500)

# Three level nesting - new example 
# Predict the output 
def f(): 
    m = 100 
    def g(): 
        n = 200 
        def h(): 
            k = 300 
            print(k) 
        h() 
        print(n) 
    g() 
    print(m)
f() 