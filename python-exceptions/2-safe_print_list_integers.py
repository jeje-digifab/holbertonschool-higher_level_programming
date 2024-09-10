#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first `x` integers in `my_list`.

    The function attempts to print each of the first `x` elements from
    `my_list`. If an element can be formatted as an integer, it is printed
    without a newline. Elements that cannot be converted to integers are
    ignored. The function also handles `IndexError` if `x` exceeds the
    length of `my_list` and re-raises it.

    Parameters:
    my_list (list): The list of elements to print. Defaults to an empty list.
    x (int): The number of elements to process from the beginning of `my_list`.
    Defaults to 0.

    Returns:
    int: The number of integers successfully printed.
    """
    count = 0

    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                continue

        print()

    except IndexError:
        raise

    return (count)
