import pytest
from solutions.HLO import hello_solution


def test_invalid_input_type():
    with pytest.raises(ValueError):
        hello_solution.hello(1)


def test_empty_input():
    with pytest.raises(ValueError):
        hello_solution.hello("")


def test_correct_output(capfd):
    hello_solution.hello("William")
    out, err = capfd.readouterr()
    assert out == "Hello William!\n"

