#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists.

    Args:
        my_list_1 (list): The first list, containing elements of any type.
        my_list_2 (list): The second list, containing elements of any type.
        list_length (int): The desired length of the resulting list.

    Returns:
        list: A new list of length `list_length` where each element
        is the result
              of the division of elements from `my_list_1` by
              corresponding elements
              from `my_list_2`. If division is not possible,
              the element will be 0.

    Exceptions:
        Prints "wrong type" if an element in the lists is not an integer
        or float.
        Prints "division by 0" if division by zero is attempted.
        Prints "out of range" if `my_list_1` or `my_list_2` is too short.
    """

    result = []

    try:
        for i in range(list_length):
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("Out of range")

            try:
                if not isinstance(my_list_1[i], (int, float)) or not \
                        isinstance(my_list_2[i], (int, float)):
                    raise TypeError("Wrong type")

                result.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("Division by 0")
                result.append(0)
            except TypeError as e:
                print(e)
                result.append(0)
    except IndexError as e:
        print(e)
        result.extend([0] * (list_length - len(result)))

    finally:
        if len(result) < list_length:
            result.extend([0] * (list_length - len(result)))
        return result
