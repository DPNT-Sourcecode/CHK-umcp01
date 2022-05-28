"""
    Contains tests for solutions.HLO module
"""
# import pytest
from solutions.HLO import hello_solution

# def test_invalid_input_type():
#     """
#     tests that invalid input types raise an error
#     """
#     with pytest.raises(ValueError):
#         hello_solution.hello(1)


# def test_empty_input():
#     """
#     tests that empty string input raises an error
#     """
#     with pytest.raises(ValueError):
#         hello_solution.hello("")


def test_correct_output():
    """
    tests that the printed output is correct
    """
    out = hello_solution.hello("William")
    assert out == "Hello, World!"





