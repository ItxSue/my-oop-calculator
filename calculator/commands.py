class CalculateCommand:
    def __init__(self, calculation, history):
        self.calculation = calculation
        self.history = history

    def execute(self):
        # Calculate first so failed operations are not saved.
        result = self.calculation.execute()
        self.history.append(
            f"{self.calculation.a} "
            f"{self.calculation.b} = {result}"
        )
        return result


class HistoryCommand:
    def __init__(self, history):
        self.history = history

    def execute(self):
        # Return a copy to protect the original history.
        return self.history.copy()