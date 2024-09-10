#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two numbers and prints the result.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float or None: The result of the division if successful,
        otherwise None.

    If division by zero is attempted, the function prints "None"
    and returns None.
    Otherwise, it prints the result of the division.
    """
    result = 0

    try:
        result = a / b

    except ZeroDivisionError:
        result = None

    finally:
        print("Inside result: {}".format(result))
        return (result)
