"""
    Contains implementation of a sum function
"""

# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(number_1: int, number_2: int) -> int:
    """
    Computes the sum of two positive integers
    Both numbers must be between 0-100.

    :param number_1: The first number to sum.
    :type number_1: int
    :param number_2:The second number to sum.
    :type number_2: int
    :raises ValueError: If either number is negative or greater than 100.
    :return: The sum of the two numbers.
    :rtype: int
    """

    if not isinstance(number_1, int):
        raise ValueError(f"number_1: ({number_1}) must be an integer.")

    if not isinstance(number_2, int):
        raise ValueError(f"number_2: ({number_2}) must be an integer.")

    if number_1 > 100 or number_1 < 0:
        raise ValueError(
            f"number_1: ({number_1}) must be greater than 0 and less than 100."
        )

    if number_2 > 100 or number_2 < 0:
        raise ValueError(
            f"number_2: ({number_2}) must be greater than 0 and less than 100."
        )

    return number_1 + number_2


