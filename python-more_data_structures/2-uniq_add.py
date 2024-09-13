#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
        my_list (list, optional): The list of integers.
        Defaults to an empty list.

    Returns:
        int: The sum of all unique integers in the list.
    """
    result = []
    for x in my_list:
        if x not in result:
            result.append(x)

    return (sum(result))
