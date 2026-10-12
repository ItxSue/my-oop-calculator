import pytest

from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def test_calculate_command():
    history = []
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)
    command = CalculateCommand(calculation, history)

    assert command.execute() == 8
    assert history == ["5 3 = 8"]


def test_failed_calculation_not_saved():
    history = []
    calculation = ArithmeticCalculation.create(6, 0, Operations.divide)
    command = CalculateCommand(calculation, history)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()

    assert history == []


def test_history_command():
    history = ["5 3 = 8"]
    command = HistoryCommand(history)

    result = command.execute()

    assert result == ["5 3 = 8"]

    # Changing the returned list must not change the original.
    result.append("10 2 = 12")
    assert history == ["5 3 = 8"]


def test_empty_history():
    command = HistoryCommand([])
    assert command.execute() == []