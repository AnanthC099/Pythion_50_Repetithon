class Gensquare_iterator:
    def __init__(self, G):
        self.G =G
    def __next__(self):
        return self.G.__next__()

class Gensquare:
    def __init__(self, N:int):
        if type(N) != int:
            raise TypeError('Bad type')
        if N <= 0:
            raise TypeError('N must be positive')
        self.N = N

    def __iter__(self):
        def get_generator(N):
            for i in range(N):
                yield i**2
        return Gensquare_iterator(get_generator(self.N))
    

# This loop should print squares of all numbers from 0 to 7 
for x in Gensquare(8):
    print(x)  
