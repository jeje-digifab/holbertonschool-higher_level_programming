#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    del_list = my_list[:]
    if idx < 0 or idx >= len(del_list):
        return my_list
    else:
        del_list.pop(idx)
        return del_list


if __name__ == "__main__":
    main()
