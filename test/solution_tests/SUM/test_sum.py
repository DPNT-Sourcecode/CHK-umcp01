"""
    Contains a test class for the solutions.SUM module
"""

import pytest
from solutions.SUM import sum_solution


class TestSum:
    """
    Implements test functions for solutions.SUM.compute
    """

    def test_sum(self):
        """
        test that simple addition works
        """
        assert sum_solution.compute(1, 2) == 3

    def test_negative_input(self):
        """
        test that negative input raises an error
        """
        with pytest.raises(ValueError):
            sum_solution.compute(-1, 2)

    def test_input_greater_than_100(self):
        """
        test that numbers greater than 100 raise an error
        """
        with pytest.raises(ValueError):
            sum_solution.compute(101, 2)

    def test_invalid_input_type(self):
        """
        test that numbers greater than 100 raise an error
        """
        with pytest.raises(ValueError):
            sum_solution.compute("two", "one")




