class Gensquare_iterator: 
    def __init__(self, G): 
        self.G = G 
    def __next__(self): 
        return self.G.__next__() 

class Gensquare: 
    def __init__(self, N): 
        self.N = N 

    def __iter__(self): 
        def get_generator(N): 
            for i in range(N): 
                yield i**2 
        return Gensquare_iterator(get_generator(self.N))


G = Gensquare(8)

print("Gensquare is an iterator class which implements read semantics")
print("Therefore, we can iterator on single object of Gensquare as many times as we want")
print("Iterating for the first time")
for x in G: 
    print(x) 
print("Iterating for the second time")
for x in G: 
    print(x) 
print("Iterating for the third time")
for x in G: 
    print(x) 