"""
    Contains implementation of a checkout function.
"""

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
from enum import Enum
from typing import DefaultDict


class DealType(Enum):
    """
    Enum that stores the various types of offer available at checkout
    """

    MULTI_BUY = 1
    FREE_ITEM = 2


COSTS: dict = {
    "A": {
        "deals": {
            DealType.MULTI_BUY: [{"count": 5, "cost": 200}, {"count": 3, "cost": 130}],
        },
        "cost": 50,
    },
    "B": {"deals": {DealType.MULTI_BUY: [{"count": 2, "cost": 45}]}, "cost": 15},
    "C": {"cost": 20},
    "D": {"cost": 15},
    "E": {
        "cost": 40,
        "deals": {DealType.FREE_ITEM: [{"count": 2, "free_item_sku": "B"}], "cost": 30},
    },
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

    code_counts: DefaultDict = defaultdict(int)

    for code in skus:
        if not code in COSTS:
            return -1
        code_counts[code] += 1

    total_cost = 0
    for code, count in code_counts.items():
        total_cost += calculate_cost(code, count)
    return total_cost


def calculate_free_items(code_counts: DefaultDict):
    for code, count in code_counts.items():


def calculate_cost(code: str, count: int) -> int:
    """
    Calculates total cost of a certain count of a single sku code
    Including multiple-buy offers.

    :param code: the sku code to calculate cost for
    :type code: str
    :param count: the count of this sku code
    :type count: int
    :return: the total cost of this number of sku-code item
             including discounts
    :rtype: int
    """
    cost_data: dict = COSTS[code]

    if "deals" in cost_data:
        code_cost = 0
        remainder = count
        deals = cost_data["deals"]
        if DealType.MULTI_BUY in deals:
            for deal in deals[DealType.MULTI_BUY]:
                code_cost += (remainder // deal["count"]) * deal["cost"]
                remainder = remainder % deal["count"]
        code_cost += remainder * cost_data["cost"]

        return code_cost

    return count * cost_data["cost"]




