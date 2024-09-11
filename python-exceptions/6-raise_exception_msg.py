#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise a NameError exception with the provided message.

    Args:
        message (str): The message to be included in the NameError.
                       Defaults to an empty string.

    Raises:
        NameError: Exception raised with the specified message.
    """
    raise NameError(message)
