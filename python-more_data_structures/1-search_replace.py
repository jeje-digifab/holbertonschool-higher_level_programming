#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for idx, item in enumerate(my_list):
        if item == search:
            new_list[idx] = replace
    return new_list


if __name__ == "__main__":
    main()
