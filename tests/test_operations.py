import pytest

from calculator.operations import Add, Subtract, Multiply, Divide


def test_add():
    operation = Add(2, 3)
    assert operation.calculate() == 5


def test_subtract():
    operation = Subtract(5, 3)
    assert operation.calculate() == 2


def test_multiply():
    operation = Multiply(4, 3)
    assert operation.calculate() == 12


def test_divide():
    operation = Divide(10, 2)
    assert operation.calculate() == 5