#!/usr/bin/python3
"""Module compiled with python3"""


def write_file(filename="", text=""):
    """
    Writes text to a file and returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        number_of_chars = file.write(text)

    return number_of_chars


if __name__ == "__main__":
    main()
