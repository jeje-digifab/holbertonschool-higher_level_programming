#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0:
        return my_list
    else:
        for num in range(len(new_list)):
            if num == idx:
                new_list[num] = element
                break

        return new_list


if __name__ == "__main__":
    main()
