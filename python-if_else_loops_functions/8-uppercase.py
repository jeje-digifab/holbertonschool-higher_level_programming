#!/usr/bin/python3


def uppercase(str):

    result = ""
    for i in range(len(str)):
        char = str[i]
        if (char >= 'a' and char <= 'z'):
            result += chr(ord(char) - 32)
        else:
            result += char

    print("{}".format(result))
