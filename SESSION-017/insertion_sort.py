def insertion_sort(L: list[int]) -> None:
    if type(L) != list:
        raise TypeError('Bad type')
    if len(L) == 0:
        return None
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i > -1 and L[i] > key:
            L[i+1] = L[i]
            i = i - 1
        L[i+1] = key


L = [50, 40, 30, 20, 10]
print(L)
insertion_sort(L)
print(L) 
