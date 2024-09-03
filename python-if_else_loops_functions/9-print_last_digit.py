#!/usr/bin/python3

def print_last_digit(number):
    """
    Print and return the last digit of a number.

    Args:
        number (int): The input number.

    Returns:
        int: The last digit of the number.
    """

    last_digit = abs(number) % 10
    print(f"{last_digit}", end="")
    return last_digit
