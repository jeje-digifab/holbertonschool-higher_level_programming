#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            print("{}".format(""), end="")
    print()
    return count


if __name__ == "__main__":
    main()
