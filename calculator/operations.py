class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Add(Calculation):
    def calculate(self):
        return self.a + self.b


class Subtract(Calculation):
    def calculate(self):
        return self.a - self.b


class Multiply(Calculation):
    def calculate(self):
        return self.a * self.b


class Divide(Calculation):
    def calculate(self):
        return self.a / self.b