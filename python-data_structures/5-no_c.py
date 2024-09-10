#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all occurrences of the characters 'c' and 'C'
    from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: A new string with 'c' and 'C' removed.
    """

    new_str = ""
    for letter in my_string:
        if letter != "c" and letter != "C":
            new_str += letter

    return (new_str)
