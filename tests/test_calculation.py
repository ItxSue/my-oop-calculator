import pytest

from calculator.calculation import Calculation, ArithmeticCalculation
from calculator.operations import Operations


def test_calculation_factory():
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)

    assert isinstance(calculation, ArithmeticCalculation)
    assert calculation.a == 5
    assert calculation.b == 3
    assert calculation.operation == Operations.add
    assert calculation.execute() == 8


def test_different_operations():
    assert ArithmeticCalculation.create(
        5, 3, Operations.subtract
    ).execute() == 2

    assert ArithmeticCalculation.create(
        5, 3, Operations.multiply
    ).execute() == 15

    assert ArithmeticCalculation.create(
        6, 3, Operations.divide
    ).execute() == 2


def test_abstract_calculation():
    with pytest.raises(TypeError):
        Calculation(5, 3, Operations.add)