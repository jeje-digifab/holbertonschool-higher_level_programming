#!/usr/bin/python3

from variable_load_5 import a

"""
This script imports the variable 'a' from the module 'variable_load_5.py'
and prints its value.

Requirements:
1. The variable 'a' is imported from 'variable_load_5.py'.
2. No usage of wildcard imports (e.g., `*`) or `__import__`.
3. The code inside the `if __name__ == "__main__":` block ensures that
the script does not execute
   when the module is imported in another script, and only executes when
   run directly.
"""

if __name__ == "__main__":
    print(a)
