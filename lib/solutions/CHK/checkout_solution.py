"""
    Contains implementation of a checkout function.
"""

# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
from enum import Enum
from typing import DefaultDict
import copy


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
    "B": {"deals": {DealType.MULTI_BUY: [{"count": 2, "cost": 45}]}, "cost": 30},
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

    calculate_free_items(code_counts)

    total_cost = 0
    for code, count in code_counts.items():
        total_cost += calculate_cost(code, count)
    return total_cost


def calculate_free_items(code_counts: DefaultDict):
    """
    Checks for offers that include free items,
    removing them from the count if applicable

    :param code_counts: a dictionary of code SKU to count pairs
    :type code_counts: DefaultDict
    """

    code_counts = copy.deepcopy(code_counts)

    for code, count in code_counts.items():
        cost_data: dict = COSTS[code]
        if not ("deals" in cost_data and DealType.FREE_ITEM in cost_data["deals"]):
            continue
        for deal in cost_data["deals"][DealType.FREE_ITEM]:
            code_counts[deal["free_item_sku"]] = max(
                0, code_counts[deal["free_item_sku"]] - count // deal["count"]
            )


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








