#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            raise ZeroDivisionError
        if a == 0 and b == 0:
            div = 0.0
        else:
            div = a / b
            if div.is_integer():
                div = int(div)
    except (ValueError, TypeError):
        div = None
        print("Inside result: {:s}".format("None\n"), end="")
    except ZeroDivisionError:
        div = None
        print("Inside result: {:s}".format("None\n"), end="")
    finally:
        if div is not None:
            if isinstance(div, int):
                div = float(div)
            print("Inside result: {:.1f}\n".format(div), end="")
    return div


if __name__ == "__main__":
    main()
