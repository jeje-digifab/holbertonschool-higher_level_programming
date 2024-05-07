#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_dg = number % 10
else:
    last_dg = number % -10
if last_dg == 0:
    print(f"Last digit of {number} is {last_dg} and is 0")
elif last_dg > 6:
    print(f"Last digit of {number} is {last_dg} and is greater than 5")
elif last_dg < 5:
    print(f"Last digit of {number} is {last_dg} and is less than 6 and not 0")
