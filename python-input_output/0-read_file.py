#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to the standard
    output.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print("{}".format(f.read()), end="")
