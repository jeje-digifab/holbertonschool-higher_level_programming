#!/usr/bin/python3

"""
This script is executed using the Python 3 interpreter.

It prints all lowercase letters of the English alphabet
from 'a' to 'z', excluding the letters 'e' and 'q'.
The letters are printed without a newline in between.
"""

print(''.join(chr(letter)
      for letter in range(97, 123) if letter not in (101, 113)))
