"""
    Contains tests for solutions.CHK module
"""

import pytest
from solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize("skus,expected", [("A", 50), ("B", 30), ("C", 20), ("D", 15)])
def test_prices(skus, expected):
    """
    Tests that valid SKU codes return their expected costs
    """
    assert checkout(skus) == expected


@pytest.mark.parametrize(
    "skus,expected",
    [
        ("AAA", 130),
        ("AA", 100),
        ("AAAAA", 200),
        ("AAAAAAAA", 330),
        ("AAAAAAAAA", 380),
        ("BB", 45),
        ("BBB", 75),
    ],
)
def test_offers(skus, expected):
    """
    Tests that multiple-purchase offers are calculated correctly
    """
    assert checkout(skus) == expected


def test_invalid_input():
    """
    Tests that incorrect string input returns -1
    """
    assert checkout("aIp@;") == -1


def test_invalid_input_type():
    """
    Tests that incorrect input types return -1
    """
    assert checkout(1) == -1


