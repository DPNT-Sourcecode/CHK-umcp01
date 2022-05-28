# noinspection PyUnusedLocal
# skus = unicode string

VALID_INPUT = (
    "A",
    "B",
    "C",
    "D"
)
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1
    raise NotImplementedError()

