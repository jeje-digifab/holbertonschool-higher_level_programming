#!/usr/bin/python3

for first in range(9):
    for sec in range(10):
        if first < sec:
            if first == 8 and sec == 9:
                print("{}{}".format(first, sec), end="\n")
            else:
                print("{}{}".format(first, sec), end=", ")
