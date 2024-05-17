#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        number = isinstance(my_list[i], int)
        if number:
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except IndexError:
                print("{}".format(""), end="")
    print()
    return count


if __name__ == "__main__":
    main()
