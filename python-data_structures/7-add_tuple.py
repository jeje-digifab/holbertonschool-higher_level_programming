#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise, ensuring each tuple has exactly two elements.
    If a tuple has fewer than two elements, it is padded with zeros.
    If a tuple has more than two elements, only the first two elements
    are used.

    Args:
        tuple_a (tuple): The first tuple, default is an empty tuple.
        tuple_b (tuple): The second tuple, default is an empty tuple.

    Returns:
        tuple: A tuple containing the element-wise sum of the two tuples.
    """

    # Handle the case where tuple_a has fewer than two elements
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            new_tuple_a = (0, 0)
        else:
            new_tuple_a = (tuple_a[0], 0)
    else:
        new_tuple_a = tuple_a[:2]

    # Handle the case where tuple_b has fewer than two elements
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            new_tuple_b = (0, 0)
        else:
            new_tuple_b = (tuple_b[0], 0)
    else:
        new_tuple_b = tuple_b[:2]

    # Add the elements of new_tuple_a and new_tuple_b element-wise
    my_tuple = tuple(map(lambda x, y: x + y, new_tuple_a, new_tuple_b))

    # Return the resulting tuple
    return (my_tuple)
