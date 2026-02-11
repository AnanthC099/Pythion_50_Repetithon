# def statement general format
def function_name(formal_parameter_list):
    statement-1
    statement-2
    .
    .
    .
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



