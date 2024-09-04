#!/usr/bin/python3

"""
This script is executed using the Python 3 interpreter.

It prints all lowercase letters of the English alphabet
from 'a' to 'z' without a newline in between.
"""

for letter in range(97, 123):
    print('{}'.format(chr(letter)), end='')
