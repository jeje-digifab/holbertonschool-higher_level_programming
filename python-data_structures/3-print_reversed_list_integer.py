#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints the elements of a list in reverse order.

    Args:
        my_list (list): A list of integers. Defaults to an empty list.

    Returns:
        None
    """
    new_list = my_list[::-1]
    for number in new_list:
        print("{}".format(number))
