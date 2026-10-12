class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Add(Calculation):
    def calculate(self):
        return self.a + self.b

    def __str__(self):
        return f"Add: {self.a} + {self.b} = {self.calculate()}"


class Subtract(Calculation):
    def calculate(self):
        return self.a - self.b

    def __str__(self):
        return f"Subtract: {self.a} - {self.b} = {self.calculate()}"


class Multiply(Calculation):
    def calculate(self):
        return self.a * self.b


class Divide(Calculation):
    def calculate(self):
        return self.a / self.b

class Operations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b