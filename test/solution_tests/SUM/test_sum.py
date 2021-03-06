"""
    Contains a test class for the solutions.SUM module
"""

import pytest
from solutions.SUM import sum_solution


def test_sum():
    """
    test that simple addition works
    """
    assert sum_solution.compute(1, 2) == 3


def test_negative_input():
    """
    test that negative input raises an error
    """
    with pytest.raises(ValueError):
        sum_solution.compute(-1, 2)


def test_input_greater_than_100():
    """
    test that numbers greater than 100 raise an error
    """
    with pytest.raises(ValueError):
        sum_solution.compute(101, 2)


def test_invalid_input_type():
    """
    test that numbers greater than 100 raise an error
    """
    with pytest.raises(ValueError):
        sum_solution.compute("two", "one")
