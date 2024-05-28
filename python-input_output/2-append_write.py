#!/usr/bin/python3
"""Module compiled with python3"""


def append_write(filename="", text=""):
    """
    This function appends text to the end of a specified file.

    :param filename: The name of the file to append text to.
    :param text: The text to append to the file.
    :return: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        number_of_chars = file.write(text)

    return number_of_chars


if __name__ == "__main__":
    main()
