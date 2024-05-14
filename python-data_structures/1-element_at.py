#!/usr/bin/python3


def element_at(my_list, idx):
    for num in range(len(my_list)):
        if idx < 0:
            print("{}".format(None))
        else:
            if num == idx:
                print("Element at index {} is {}".format(idx, num))
            elif len(my_list) >= idx:
                return my_list[idx]


if __name__ == "__main__":
    main()
