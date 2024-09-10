#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer with the format "{:d}".

    Args:
        value: The value to print. It should be an integer.

    Returns:
        True if the value was successfully printed as an integer.
        False if a ValueError was raised, indicating the value is
        not an integer.
    """
    try:
        print("{:d}".format(value))
        return True

    except ValueError:
        return False
