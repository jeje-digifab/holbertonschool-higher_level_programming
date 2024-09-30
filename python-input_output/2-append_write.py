#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def append_write(filename="", text=""):
    """
    Appends the specified text to a file with UTF-8 encoding.

    Args:
        filename (str): The name of the file where the text will be appended.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
