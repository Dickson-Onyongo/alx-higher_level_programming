#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Return the addition of two numbers.

    Args:
        a(int or float): The first number.
        b(int or float): The second number.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeErrpr: If either a or b is not an integer or float.
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance:
        raise TypeError("b must be an integer")
    else:

        print(a + b)
