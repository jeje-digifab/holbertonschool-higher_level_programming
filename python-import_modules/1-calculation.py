#!/usr/bin/python3
"""
This module imports basic arithmetic functions (add, sub, mul, div)
from 'calculator_1' and performs operations on two integers.
"""

from calculator_1 import add, sub, mul, div

a = 10
b = 5


if __name__ == "__main__":
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
