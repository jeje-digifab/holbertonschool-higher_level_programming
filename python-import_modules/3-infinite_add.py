#!/usr/bin/python3
import sys

sum = 0

valid_args_found = False
for i in range(1, len(sys.argv)):
    is_positive_integer = sys.argv[i].isdigit()
    is_negative_integer = sys.argv[i][0] == '-' and sys.argv[i][1:].isdigit()

    if is_positive_integer or is_negative_integer:
        sum += int(sys.argv[i])
        valid_args_found = True

if valid_args_found:
    print(sum)
else:
    print("0")
