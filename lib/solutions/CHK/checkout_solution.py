"""
    Contains implementation of a checkout function.
"""

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict

COSTS = {
    "A": {"deal": {"count": 3, "cost": 130}, "cost": 50},
    "B": {"deal": {"count": 2, "cost": 45}, "cost": 30},
    "C": {"cost": 20},
    "D": {"cost": 15},
}


def checkout(skus: str) -> int:
    """
    Converts a string of SKU Stock Keeping Units to their total cost,
    checking for applicable deals

    :param skus: A string containing SKU Stock Keeping Units
    :type skus: str
    :return: The total cost of the SKU Stock Keeping Units
             or -1 if invalid input is detected
    :rtype: int
    """
    if not isinstance(skus, str):
        return -1

    code_counts = defaultdict(int)

    for code in skus:
        if not code in COSTS.keys():
            return -1
        code_counts[code] += 1

    total_cost = 0
    for code, count in code_counts.items():
        cost_data = COSTS[code]
        if "deal" in cost_data:
            total_cost += (
                (count // cost_data["deal"]["count"]) * cost_data["deal"]["cost"]
            ) + (count % cost_data["deal"]["count"]) * cost_data["cost"]
        else:
            total_cost += count * cost_data["cost"]

    return total_cost







