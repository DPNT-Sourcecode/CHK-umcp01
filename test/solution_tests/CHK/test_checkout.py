"""
    Contains tests for solutions.CHK module
"""

import pytest
from solutions.CHK.checkout_solution import checkout


+------+-------+------------------------+
|     | 3A for 130, 5A for 200 |
|     | 2B for 45              |
|     |                        |
|     |                        |
|     | 2E get one B free      |
|     | 2F get one F free      |
|     |                        |
|     | 5H for 45, 10H for 80  |
|     |                        |
|     |                        |
|     | 2K for 150             |
|     |                        |
|     |                        |
|     | 3N get one M free      |
|     |                        |
|     | 5P for 200             |
|     | 3Q for 80              |
|     | 3R get one Q free      |
|     |                        |
|     |                        |
|     | 3U get one U free      |
|     | 2V for 90, 3V for 130  |
|     |                        |
|     |                        |
|     |                        |
|     |                        |
+------+-------+------------------------+


@pytest.mark.parametrize(
    "skus,expected", [("A",50),
("B",30),
("C",20),
("D",15),
("E",40),
("F",10),
("G",20),
("H",10),
("I",35),
("J",60),
("K",80),
("L",90),
("M",15),
("N",40),
("O",10),
("P",50),
("Q",30),
("R",50),
("S",30),
("T",20),
("U",40),
("V",50),
("W",20),
("X",90),
("Y",10),
("Z",50),]
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

