"""
    Contains implementation of a checkout function.
"""

# noinspection PyUnusedLocal
# skus = unicode string

import copy
import json
from collections import defaultdict
from enum import Enum


class DealType(Enum):
    """
    Enum that stores the various types of offer available at checkout
    """

    MULTI_BUY = 1
    FREE_ITEM = 2


class SKUData:

    data: dict

    def __init__(self) -> None:
        f = open("sku_data.json")
        data = json.load(f)

    def calculate_free_items(self, code_counts: dict) -> dict:
        """
        Checks for offers that include free items,
        removing them from the count if applicable

        :param code_counts: a dictionary of code SKU to count pairs
        :type code_counts: dict
        :return: the new calculated dictionary of code counts
        :rtype: dict
        """

        code_counts_calculated = copy.deepcopy(code_counts)

        for code, count in code_counts.items():
            cost_data: dict = self.data[code]
            if not ("deals" in cost_data and DealType.FREE_ITEM in cost_data["deals"]):
                continue
            for deal in cost_data["deals"][DealType.FREE_ITEM]:
                code_counts_calculated[deal["free_item_sku"]] = max(
                    0,
                    code_counts_calculated[deal["free_item_sku"]]
                    - count // deal["count"],
                )

        return code_counts_calculated

    def calculate_cost(self, code: str, count: int) -> int:
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
        cost_data: dict = self.data[code]

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

    def calculate_cost(self, skus) -> int:
        """
        Converts a string of SKU Stock Keeping Units to their total cost,
        checking for applicable deals

        :param skus: An iterable containing SKU Stock Keeping Unit codes
        :return: The total cost of the SKU Stock Keeping Units
                or -1 if invalid input is detected
        :rtype: int
        """
        code_counts: dict = defaultdict(int)

        for code in skus:
            if not code in self.data:
                return -1
            code_counts[code] += 1

        code_counts = self.calculate_free_items(code_counts)

        total_cost = 0
        for code, count in code_counts.items():
            total_cost += self.calculate_cost(code, count)
        return total_cost


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

    sku_data = SKUData()
    return sku_data.calculate_cost(skus)




