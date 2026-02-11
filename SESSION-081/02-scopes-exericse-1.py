D1 = {'a' : 100, 'b' : 200, 'c' : 300}
D2 = {'b':2000, 'e': 5000, 'g': 5000}

D = {} 

for key in D1: 
    if key in D2: 
        D[key] = D2[key] 
    else: 
        D[key] = D1[key] 

for key in D2: 
    if key not in D1: 
        D[key] = D2[key]

def my_intersection(S1:set, S2:set) -> set: 
    S = set() 
    for x in S1: 
        if x in S2: 
            S.add(x)
    return S 

class Node: 
    def __init__(self, init_data): 
        self.data = init_data 
        self.prev = None 
        self.next = None 
