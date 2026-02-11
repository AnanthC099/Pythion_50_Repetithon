"""
Simplified version of SESSION-042/def-statement-repeatithon.py (linear_search)

ORIGINAL: Uses type(L) != list, type(search_data) != int,
type(x) != int inside loop for every element.
SIMPLIFIED: Uses isinstance(), validates once at entry.
"""


def linear_search(L: list[int], search_data: int) -> bool:
    if not isinstance(L, list):
        raise TypeError("Expected a list")
    if not isinstance(search_data, int):
        raise TypeError("Search data must be int")

    for x in L:
        if not isinstance(x, int):
            raise TypeError("All list elements must be int")
        if x == search_data:
            return True
    return False


# --- Testing ---
print(linear_search([10, 20, 30, 40, 50], 30))  # True
print(linear_search([10, 20, 30, 40, 50], 99))  # False
