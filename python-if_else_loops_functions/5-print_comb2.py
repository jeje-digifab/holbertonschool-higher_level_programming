#!/usr/bin/python3

"""
Prints numbers from 00 to 99, separated by a comma and a space,
then prints "99" followed by a newline.
"""

for number in range(99):
    print(f"{number:02d}", end=", ")
print("99\n")
