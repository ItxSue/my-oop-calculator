from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def main():
    # Match each command to its arithmetic operation (Strategy Pattern).
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }

    history = []

    print("Calculator started!")
    print("Commands: add, subtract, multiply, divide, history, exit")

    while True:
        try:
            user_input = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("Goodbye!")
            break

        parts = user_input.split()

        if not parts:
            print("Please enter a command.")
            continue

        command_name = parts[0]

        if command_name == "exit":
            if len(parts) != 1:
                print("Exit does not take any operands.")
                continue
            print("Goodbye!")
            break

        if command_name == "history":
            if len(parts) != 1:
                print("History does not take any operands.")
                continue

            entries = HistoryCommand(history).execute()

            if not entries:
                print("No history yet.")
            else:
                for entry in entries:
                    print(entry)
            continue

        if command_name not in operations:
            print("Unknown command.")
            continue

        if len(parts) != 3:
            print("Please enter exactly two numbers.")
            continue

        try:
            a = float(parts[1])
            b = float(parts[2])

            operation = operations[command_name]
            calculation = ArithmeticCalculation.create(a, b, operation)
            command = CalculateCommand(calculation, history)

            print(command.execute())

        except ValueError as error:
            print(f"Error: {error}")