#!/usr/bin/python3

def uppercase(str):

    """
    Convert all lowercase letters in a string
    to uppercase and print the result.

    Args:
        str (str): The input string to be converted.

    Returns:
        None
    """

    for letter in str:
        if letter >= "a" and letter <= "z":
            new_str = (ord(letter)) - 32
        else:
            new_str = (ord(letter))

        print(f"{chr(new_str)}", end="")

    print()
