"""
    Contains implementation of a checkout function.
"""

# noinspection PyUnusedLocal
# skus = unicode string

import code
import copy
import json
from collections import defaultdict
from itertools import product
from pathlib import Path


class SKUData:
    """
    Class that contains SKU price and deal information
    as well as functions for calculating checkout costs
    """

    data: dict
    deals: dict
    data_file_path = Path(__file__).parent.absolute() / "sku_data.json"
    deals_file_path = Path(__file__).parent.absolute() / "sku_deals.json"

    deal_types = {"free_item": "FREE_ITEM", "multi_buy": "MULTI_BUY"}

    def __init__(self) -> None:
        self.data = json.loads(self.data_file_path.read_bytes())
        self.deals = json.loads(self.deals_file_path.read_bytes())

    def _calculate_free_items(self, code_counts: dict) -> dict:
        """
        Checks for offers that include free items,
        removing them from the count if applicable

        :param code_counts: a dictionary of code SKU to count pairs
        :type code_counts: dict
        :return: the new calculated dictionary of code counts
        :rtype: dict
        """

        code_counts_calculated = copy.deepcopy(code_counts)

        self._calculate_group_buy(code_counts_calculated)

        for code, count in code_counts.items():
            if not code in self.deals[self.deal_types["free_item"]]:
                continue
            for deal in self.deals[self.deal_types["free_item"]][code]:
                code_counts_calculated[deal["free_item_sku"]] = max(
                    0,
                    code_counts_calculated[deal["free_item_sku"]]
                    - count // deal["count"],
                )

        return code_counts_calculated

    def _calculate_group_buy(self, code_counts: dict, items: list = None) -> bool:
        if not items:
            items = []
            for sku, count in code_counts.items():
                for _ in range(count):
                    items.append(sku)

        if not items or len(items) < 3:
            return

        found_deal = False
        for group_buy in self.deals["GROUP_BUY"]:
            for group_buy_ids in product(group_buy["ids"], repeat=group_buy["count"]):
                if not set(group_buy_ids).issubset(items):
                    continue

                found_deal = True
                for id in group_buy_ids:
                    items.remove(id)
                    code_counts[id] = code_counts[id] - 1
                    if code_counts[id] <= 0:
                        code_counts.pop(id)

        if found_deal and len(items) > 2:
            self._calculate_group_buy(code_counts, items)

    def _calculate_multi_buy(self, code: str, count: int):
        cost_data: dict = self.data[code]
        code_cost = 0
        remainder = count
        for deal in self.deals[self.deal_types["multi_buy"]][code]:
            code_cost += (remainder // deal["count"]) * deal["cost"]
            remainder = remainder % deal["count"]
        code_cost += remainder * cost_data["cost"]

        return code_cost

    def _calculate_sku_count_cost(self, code: str, count: int) -> int:
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
        if code in self.deals[self.deal_types["multi_buy"]]:
            return self._calculate_multi_buy(code, count)

        cost_data: dict = self.data[code]
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

        code_counts = self._calculate_free_items(code_counts)

        total_cost = 0
        for code, count in code_counts.items():
            total_cost += self._calculate_sku_count_cost(code, count)
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
