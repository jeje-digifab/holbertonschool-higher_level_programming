#!/usr/bin/python3
"""
This script contains a function to print a square with a given size.
"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i != "." and i != "?" and i != ":":
            print("{}".format(i), end="")

        else:
            print("{}".format(i), end="\n")
            print()


