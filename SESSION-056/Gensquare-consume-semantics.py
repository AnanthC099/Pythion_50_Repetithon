class Gensquare: 
    def __init__(self, N): 
        self.N = N 
        def get_generator(N): 
            for i in range(N): 
                yield i ** 2 
        self.G = get_generator(self.N)

    def __iter__(self): 
        return self 

    def __next__(self): 
        return self.G.__next__() 


print('Gensquare is an iterator which is implemented using consume semantics')
print('Therefore we can iterator on its object only once')

G = Gensquare(8)
print('Iterating for the first time')
for x in G: 
    print(x) 
print('Iterating for the second time')
for x in G: 
    print(x) 
print('----SECOND TIME ITERATION OVER-----')