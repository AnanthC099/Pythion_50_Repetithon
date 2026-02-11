def find_all_occurrences(L: list, element: any) -> list[int]:
    index_list = []
    start_index = 0
    current_index = 0
    while element in L[start_index : len(L)]:
        current_index = L.index(element, start_index)
        index_list.append(current_index)
        start_index = current_index + 1
    return index_list

L = [10, 20, 30, 10, 20, 40, 20, 10, 30, 50, 60, 30, 20, 40]

all_indices_20 = find_all_occurrences(L, 20)
all_indices_10 = find_all_occurrences(L, 10)
all_indices_30 = find_all_occurrences(L, 30)
all_indices_40 = find_all_occurrences(L, 40)
all_indices_50 = find_all_occurrences(L, 50)
all_indices_60 = find_all_occurrences(L, 60)

i = 0
while i < len(L):
    print(i, L[i], sep='\t')
    i = i + 1 

print('All indices for data value 10:', all_indices_10)
print('All indices for data value 20:', all_indices_20)
print('All indices for data value 30:', all_indices_30)
print('All indices for data value 40:', all_indices_40)
print('All indices for data value 50:', all_indices_50)
print('All indices for data value 60:', all_indices_60)

