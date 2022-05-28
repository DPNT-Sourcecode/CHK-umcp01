"""
    Contains tests for solutions.CHK module
"""


"""
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+
"""

import pytest
from solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize("skus,expected", [("A", 50), ("B", 30), ("C", 20), ("D", 15)])
def test_prices(skus, expected):
    assert checkout(skus) == expected


@pytest.mark.parametrize("skus,expected", [("AAA", 130), ("BB", 45), ("AAAAA", 230), ("BBB", 75)])
def test_offers(skus, expected):
    assert checkout(skus) == expected


def test_invalid_input():
    assert checkout("aIp@;") == -1


def test_invalid_input_type():
    assert checkout(1) == -1


