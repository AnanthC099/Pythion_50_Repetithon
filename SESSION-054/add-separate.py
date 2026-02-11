# Warm up exercise for logic based interviews

global_list = [] 
def add(container):
    for x in container:
        if '__iter__' in dir(type(x)):
            add(x)
        else:
            global_list.append(x) 
            
print(global_list)

T = (10, 20, (30, 40, (50, 60), 70), [(100, 200, 300), (400, 500)])

add(T)

print(global_list)
