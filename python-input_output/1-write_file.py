#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def write_file(filename="", text=""):
    """
    Writes the specified text to a file with UTF-8 encoding.

    Args:
        filename (str): The name of the file where the text will be written.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
