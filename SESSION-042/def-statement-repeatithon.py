# def statement general format
def function_name(formal_parameter_list):
    statement-1
    statement-2
    # .
    # .
    # .
    statement-N
#------------------------------------------------------------------
def linear_search(L, search_data: int) -> bool:
    if type(L) != list:
        raise TypeError('Bad type for L')
    if type(search_data) != int:
        raise TypeError('Bad type for search data')

    for x in L:
        if type(x) != int:
            raise TypeError('Bad type for input elements')
        if x == search_data:
            return True
    return False
#------------------------------------------------------------------

# Driver code to test linear_search
if __name__ == '__main__':
    # Test 1: search_data found in list
    result = linear_search([10, 20, 30, 40, 50], 30)
    print(f'Test 1 - search for 30 in [10,20,30,40,50]: {result}')  # True

    # Test 2: search_data not found in list
    result = linear_search([10, 20, 30, 40, 50], 99)
    print(f'Test 2 - search for 99 in [10,20,30,40,50]: {result}')  # False

    # Test 3: empty list
    result = linear_search([], 5)
    print(f'Test 3 - search for 5 in []: {result}')  # False

    # Test 4: single-element list, found
    result = linear_search([7], 7)
    print(f'Test 4 - search for 7 in [7]: {result}')  # True

    # Test 5: single-element list, not found
    result = linear_search([7], 3)
    print(f'Test 5 - search for 3 in [7]: {result}')  # False

    # Test 6: TypeError when L is not a list
    try:
        linear_search('hello', 1)
    except TypeError as e:
        print(f'Test 6 - L is a string: {e}')  # Bad type for L

    # Test 7: TypeError when search_data is not an int
    try:
        linear_search([1, 2, 3], 'a')
    except TypeError as e:
        print(f'Test 7 - search_data is a string: {e}')  # Bad type for search data

    # Test 8: TypeError when list contains a non-int element
    try:
        linear_search([1, 2, 'three', 4], 4)
    except TypeError as e:
        print(f'Test 8 - list has non-int element: {e}')  # Bad type for input elements


