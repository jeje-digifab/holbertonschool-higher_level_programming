#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Check if the index is out of bounds.
    If the index is negative or greater than or equal to the list length,
    return None.
    """
    if idx < 0 or idx >= len(my_list):
        return None

    """
    If the index is within bounds, return the element at that index
    in the list.
    """
    return (my_list[idx])
