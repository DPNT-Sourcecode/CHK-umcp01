# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict

VALID_INPUT = (
    "A",
    "B",
    "C",
    "D"
)
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    code_counts = defaultdict(int)

    for code in skus:
        if not code in VALID_INPUT:
            return -1
        code_counts[code] += 1

    raise NotImplementedError()



