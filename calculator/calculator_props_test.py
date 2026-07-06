"""More calculator tests, kept as a separate target from calculator_test."""

from calculator import calculator


def test_add():
    assert calculator.add(2, 2) == 4


def test_subtract():
    assert calculator.subtract(5, 3) == 2
