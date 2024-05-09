#!/usr/bin/python3
import sys


def main():

    sum = 0

    valid_args_found = False
    for i in range(1, len(sys.argv)):
        positive_integer = sys.argv[i].isdigit()
        negative_integer = sys.argv[i][0] == '-' and sys.argv[i][1:].isdigit()

        if positive_integer or negative_integer:
            sum += int(sys.argv[i])
            valid_args_found = True

    if valid_args_found:
        print(sum)
    else:
        print("0")


if __name__ == "__main__":
    main()
