#!/usr/bin/python3


def safe_print_division(a, b):
    div = None
    try:
        div = a / b
    except ZeroDivisionError:
        print("Inside result: {:s}".format("None\n"), end="")
        return None
    finally:
        if div is not None:
            print("Inside result: {:0.2f}\n".format(div), end="")
    return div


if __name__ == "__main__":
    main()
