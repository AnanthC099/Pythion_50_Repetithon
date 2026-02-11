L = [x for x in iterable]
L = [x for x in iterable if cond(x)]
L = [f(x) for x in iterable]
L = [f(x) for x in iterable if cond(x)]

L = [x for x in (10, 20, 30)]

L = [c for c in 'CoreCode Programming Academy']

for s in [c*5 for c in "CoreCode Programming Academy" if c.isalpha()]:
    print(s)

for capitalized_line in [line.upper() for line in open(path) if len(line) < 50]:
    print(capitalized_line)



for capitalized_line in [line.strip().upper()
                         for line in open(path)
                         if not line.startswith('#') and len(line) < 50
                         ]:
    print(capitalized_line) 
    
