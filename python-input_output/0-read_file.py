#!/usr/bin/python3
"""Module compiled with python3"""


def read_file(filename=""):
    """
    Reads a file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty
        string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")


if __name__ == "__main__":
    main()
