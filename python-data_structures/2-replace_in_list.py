#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    else:
        for num in range(len(my_list)):
            if num == idx:
                my_list[num] = element
                break

        return my_list


if __name__ == "__main__":
    main()
