#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def multiply_list_map(my_list=[], number=0):
    """
    Multiply each element in the input list by a given number using
    the map() function.

    Args:
        my_list (list): The input list of numbers.
        number (int): The number to multiply each element in the list by.

    Returns:
        list: A new list with each element multiplied by the given number.
    """
    new_list = my_list.copy()
    new_list = list(map(lambda i: i * number, new_list))
    return (new_list)
