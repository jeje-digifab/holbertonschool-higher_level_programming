#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple containing the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple where the first element is the length of the sentence,
        and the second element is the first character of the sentence.
        If the sentence is empty, the second element will be an empty string.
    """
    if len(sentence) == 0:
        return (len(sentence), None)

    return (len(sentence), sentence[:1])
