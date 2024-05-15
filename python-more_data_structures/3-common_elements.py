#!/usr/bin/python3


def common_elements(set_1, set_2):
    common_set = set_1 & set_2
    if common_set:
        return common_set
    else:
        return ""


if __name__ == "__main__":
    main()
