#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element in a list with another element.

    Args:
        my_list (list): The original list to perform the replacement on.
        search: The element to search for in the list.
        replace: The element to replace the searched element with.

    Returns:
        list: A new list with the specified element replaced.
    """

    # Create a copy of the original list to avoid modifying it directly
    new_list = my_list[:]

    # Iterate through the list and replace occurrences
    # of 'search' with 'replace'
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace

    # Return the modified list
    return (new_list)
