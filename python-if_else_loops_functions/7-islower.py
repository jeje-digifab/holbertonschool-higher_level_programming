#!/usr/bin/python3

def islower(c):
    """
    Check if a character is a lowercase letter.

    Args:
        c (str): A single character.

    Returns:
        bool: True if c is a lowercase letter, False otherwise.
    """

    if c >= "a" and c <= "z":
        return True
    else:
        return False
