#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        print(" ".join(["{:d}".format(elem) for elem in x]))


if __name__ == "__main__":
    main()
