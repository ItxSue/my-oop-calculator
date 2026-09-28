from calculator.operations import Add, Subtract
from calculator.history import History


def main():
    history = History()

    print("Calculator started.")
    print("Commands: add, subtract, history, remove, help, exit")

    while True:
        command = input("> ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        elif command == "help":
            print("Commands: add, subtract, history, remove, help, exit")

        elif command == "add":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            calculation = Add(a, b)
            history.add(calculation)

            print("Result:", calculation.calculate())

        elif command == "subtract":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            calculation = Subtract(a, b)
            history.add(calculation)

            print("Result:", calculation.calculate())

        elif command == "history":
            calculations = history.get_all()

            if not calculations:
                print("No history yet.")
            else:
                for index, calculation in enumerate(calculations, start=1):
                    print(f"{index}. {calculation}")

        elif command == "remove":
            calculations = history.get_all()

            if not calculations:
                print("No history to remove.")
            else:
                for index, calculation in enumerate(calculations, start=1):
                    print(f"{index}. {calculation}")

                number = int(input("Enter history number to remove: "))
                history.remove(number - 1)

                print("History item removed.")


if __name__ == "__main__":
    main()