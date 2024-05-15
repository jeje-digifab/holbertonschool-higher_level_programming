#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        items = sorted(a_dictionary.items())
        formatted_items = ["{}: {}".format(k, v) for k, v in items]
        result = "\n".join(formatted_items)
        print("{}".format(result))


if __name__ == "__main__":
    main()
