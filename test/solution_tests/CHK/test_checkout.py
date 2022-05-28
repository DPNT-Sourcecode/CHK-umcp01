"""
    Contains tests for solutions.CHK module
"""

import pytest
from solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize(
    "skus,expected",
    [
        ("A", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15),
        ("E", 40),
        ("F", 10),
        ("G", 20),
        ("H", 10),
        ("I", 35),
        ("J", 60),
        ("K", 70),
        ("L", 90),
        ("M", 15),
        ("N", 40),
        ("O", 10),
        ("P", 50),
        ("Q", 30),
        ("R", 50),
        ("S", 20),
        ("T", 20),
        ("U", 40),
        ("V", 50),
        ("W", 20),
        ("X", 17),
        ("Y", 20),
        ("Z", 21),
    ],
)
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
        ("EEBBB", 125),
        ("EEBBBAA", 225),
        ("FF", 20),
        ("FFF", 20),
        ("FFFF", 30),
        ("FFFFF", 40),
        ("HHHHH", 45),
        ("HHHHHHHHHH", 80),
        ("KK", 150),
        ("NNM", 95),
        ("NNNM", 120),
        ("PPPPP", 200),
        ("QQQ", 80),
        ("RRRQ", 150),
        ("UUU", 120),
        ("UUUU", 120),
        ("VV", 90),
        ("VVV", 130),
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
