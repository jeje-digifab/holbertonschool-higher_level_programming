#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace the element at a specific index in a list with a new element.

    Parameters:
    my_list (list): The list in which the element will be replaced.
    idx (int): The index of the element to replace.
    element (any): The new element to insert at the specified index.

    Returns:
    list: The modified list with the element replaced, or the original
    list if the index is out of bounds.
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
