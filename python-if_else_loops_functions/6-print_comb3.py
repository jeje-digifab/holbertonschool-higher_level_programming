#!/usr/bin/python3

"""
This script prints all possible different combinations of two digits.

- The digits must be different.
- Combinations like 01 and 10 are considered the same and only the smallest
  combination is printed.
- The numbers are printed in ascending order.
- Each combination is separated by a comma and a space, except the last one.
"""

for i in range(10):
    """
    Loop through each digit from 0 to 9.
    """
    for j in range(i + 1, 10):
        """
        Loop through the next digits starting from i+1 to avoid repeating
        combinations in different orders (e.g., 01 and 10).
        """
        if i == 8 and j == 9:
            """
            Print the last combination without a comma and space at the end.
            """
            print(f"{i}{j}")
        else:
            """
            Print the combination with a comma and a space for all except
            the last one.
            """
            print(f"{i}{j}, ", end="")
