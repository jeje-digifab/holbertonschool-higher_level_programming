#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Removes an element from a list at a specified index.

    Args:
        my_list (list): The list from which an element will be removed.
        idx (int): The index of the element to remove.

    Returns:
        list: The list with the specified element removed. If the index
              is out of range, the original list is returned.
    """
    # Check if the index is out of the valid range
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list if the index is invalid

    # Remove the element at the specified index
    del my_list[idx]

    # Return the modified list
    return my_list
