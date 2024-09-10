#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Returns a list of boolean values indicating whether each
    integer in the input list is divisible by 2.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of boolean values (True or False), where each
              value corresponds to whether the integer at the same
              position in the input list is divisible by 2.
    """
    new_list = []

    for number in my_list:
        if number % 2 == 0:
            # Append True if the number is divisible by 2
            new_list.append(True)
        else:
            # Append False if the number is not divisible by 2
            new_list.append(False)

    return (new_list)
