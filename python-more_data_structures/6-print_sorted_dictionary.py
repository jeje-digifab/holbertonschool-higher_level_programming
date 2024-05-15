#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    print("\n".join("{}: {}".format(k, v) for k, v in sorted(a_dictionary.items())))


if __name__ == "__main__":
    main()
