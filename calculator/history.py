class History:
    def __init__(self):
        self._calculations = []

    def add(self, calculation):
        self._calculations.append(calculation)

    def get_all(self):
        return self._calculations

    def clear(self):
        self._calculations.clear()