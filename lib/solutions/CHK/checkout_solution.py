# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict

COSTS = {
    "A": {"deal": {"count": 3, "value": 130}, "cost": 50},
    "B": {"deal": {"count": 2, "value": 45}, "cost": 30},
    "C": {"cost": 20},
    "D": {"cost": 15}
}

def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    code_counts = defaultdict(int)

    for code in skus:
        if not code in COSTS.keys():
            return -1
        code_counts[code] += 1

    total_cost = 0
    for code, count in code_counts.items():
        deal_cost = COSTS[code] /
        total_cost +=



    raise NotImplementedError()





