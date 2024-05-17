#!/usr/bin/python3


def raise_exception_msg(message=""):
    if not message:
        message = ""
    raise NameError(message)


if __name__ == "__main__":
    main()
