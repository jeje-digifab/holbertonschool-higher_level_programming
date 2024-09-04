#!/usr/bin/python3

"""
This script is executed using the Python 3 interpreter.

It prints all lowercase letters of the English alphabet
from 'a' to 'z' without a newline in between.
"""

print(''.join(chr(97 + i) for i in range(26)))
