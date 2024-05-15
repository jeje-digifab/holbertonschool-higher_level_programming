#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    a_dictionary_mul = a_dictionary.copy()
    a_dictionary_mul.update((key, value * 2) for key, value in a_dictionary.items())
    return a_dictionary_mul


if __name__ == "__main__":
    main()
