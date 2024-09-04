#!/usr/bin/python3

"""
This script is executed using the Python 3 interpreter.

It prints numbers from 0 to 98 alongside their hexadecimal
representation. The numbers are printed in the format:
<number> = 0x<hexadecimal>, with each pair on a new line.
"""

for exa in range(99):
    print(f"{exa} = 0x{exa:02x}")
