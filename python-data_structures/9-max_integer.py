#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find and return the maximum integer in a list.

    :param my_list: List of integers to evaluate (default is an empty list)
    :return: The maximum integer in the list, or None if the list is empty
    """
    # Return None if the list is empty
    if len(my_list) == 0:
        return (None)

    # Initialize the maximum value to 0
    maximum = my_list[0]

    # Iterate through each number in the list
    for number in my_list:
        # Update max if the current number is greater
        if number > maximum:
            maximum = number

    # Return the maximum value found
    return (maximum)
