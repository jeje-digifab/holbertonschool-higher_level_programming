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
    skip_next = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for idx, i in enumerate(text):
        if skip_next:
            skip_next = False
            continue
        if i in [".", ":", "?", "!"]:
            print("{:s}".format(i), end="\n")
            print()
            skip_next = True
        else:
            print("{:s}".format(i), end="")


if __name__ == "__main__":
    main()
