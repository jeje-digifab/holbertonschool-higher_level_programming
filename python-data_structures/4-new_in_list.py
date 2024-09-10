#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Create a copy of the list to avoid modifying the original one.

    If the index is out of bounds, return the unmodified copy of the list.
    Otherwise, replace the element at the specified index with the new element
    in the copied list.

    Return the modified copy of the list.
    """

    new_list = my_list[:]

    if idx < 0 or idx >= len(my_list):
        return (new_list)
    else:
        new_list[idx] = element
        return (new_list)
