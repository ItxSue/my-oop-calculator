from abc import ABC, abstractmethod
from collections.abc import Callable


class Calculation(ABC):
    def __init__(self, a: float, b: float,
                 operation: Callable[[float, float], float]):
        # Store the numbers and the selected operation.
        self.a = a
        self.b = b
        self.operation = operation

    @classmethod
    def create(cls, a, b, operation):
        # Factory method creates a new calculation.
        return cls(a, b, operation)

    @abstractmethod
    def execute(self) -> float:  # pragma: no cover
        pass


class ArithmeticCalculation(Calculation):
    def execute(self) -> float:
        # Run the operation using the stored numbers.
        return self.operation(self.a, self.b)