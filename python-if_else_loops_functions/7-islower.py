#!/usr/bin/python3

def islower(c):
    """
    Check if a character is a lowercase letter.

    Args:
        c (str): A single character.

    Returns:
        bool: True if c is a lowercase letter, False otherwise.
    """
    return ord(c) >= ord('a') and ord(c) <= ord('z')
