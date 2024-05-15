#!/usr/bin/python3


def uniq_add(my_list=[]):
    my_list = list(set(my_list))
    sum = 0
    for add in my_list:
        sum += add
    return sum


if __name__ == "__main__":
    main()
