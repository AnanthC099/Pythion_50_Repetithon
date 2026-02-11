'''
class Test: 
    def __init__(self, init_n): 
        self.N = init_n 

    def getn(self): 
        return self.N 

    def setn(self, newN): 
        self.N = newN 

t = Test(100)
print(t.getn())
t.setn(200)
print(t.getn())

t.setn(500)
t.getn()
'''
#-------------------------------------------

print('NESTED DEF STATEMENT')
def test(init_n): 
    N = init_n 

    def getn(): 
        nonlocal N 
        return N 

    def setn(newN): 
        nonlocal N 
        N = newN

    return (getn, setn)

getn, setn = test(100)

print(getn())   # 100 
setn(200)       # set 200 
print(getn())   # 200 
setn(500)
print(getn()) 



