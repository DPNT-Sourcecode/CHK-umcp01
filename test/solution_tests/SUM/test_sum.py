"""
    Contains a test class for the solutions.SUM module
"""

import pytest
from solutions.SUM import sum_solution


class TestSum:
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_negative_input(self):
        with pytest.raises(ValueError):
            sum_solution.compute(-1, 2)

    def test_input_greater_than_100(self):
        with pytest.raises(ValueError):
            sum_solution.compute(101, 2)



