#!/usr/bin/python3

for letters in range(ord('a'), ord('z')+1):
    if letters != (ord('q')) and letters != (ord("e")):
        print("{:c}".format(letters), end="")
