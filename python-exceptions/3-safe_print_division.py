#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        div = a / b
        print("Inside result: {:0.2f}\n".format(div), end="")
    except ZeroDivisionError:
        print("Inside result: None\n", end="")
        return None
    return div


if __name__ == "__main__":
    main()
