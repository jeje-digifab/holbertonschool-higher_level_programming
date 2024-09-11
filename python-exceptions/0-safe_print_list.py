#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints up to 'x' elements of a list.

    Parameters:
    my_list (list): The list to print elements from.
    x (int): The number of elements to print.

    Returns:
    int: The number of elements actually printed.
    """

    count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print()
    except IndexError:
        print()

    return (count)
