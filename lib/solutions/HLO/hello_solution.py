# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> None:

    if not isinstance(friend_name, str):
        raise ValueError("friend_name must be a String")

    print(f"Hello {friend_name}!")

