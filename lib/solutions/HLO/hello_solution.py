"""
    Contains implementation of a greeting function.
"""

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    """
    Returns a greeting in the format "Hello {friend_name}!"

    :param friend_name: the name to use in the greeting
    :type friend_name: str
    :raises ValueError: If friend_name is not a valid String.
    :return: A greeting containing the provided friend_name string
    :rtype: str
    """

    if not isinstance(friend_name, str):
        raise ValueError("friend_name must be a String.")

    if not friend_name:
        raise ValueError("friend_name must not be empty.")

    return f"Hello, {friend_name}!"

