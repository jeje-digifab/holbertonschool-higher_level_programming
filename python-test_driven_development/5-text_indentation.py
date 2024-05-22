#!/usr/bin/python3
"""Module compiled with python3"""


def text_indentation(text):
    """
    Prints the given text with indentation at the start of each new line.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""

    for char in text:
        if char in [".", "?", ":"]:
            current_line = current_line.strip()
            current_line = current_line.rstrip(" ")
            print(current_line, end="")
            print(char, end="\n\n")
            current_line = ""
        else:
            current_line += char

    if current_line:
        current_line = current_line.strip()
        current_line = current_line.rstrip(" ")
        print(current_line, end="")


if __name__ == "__main__":
    main()
