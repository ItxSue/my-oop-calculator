from calculator.operations import Add, Subtract
from calculator.history import History


def main():
    history = History()

    print("Calculator started.")
    print("Commands: add, subtract, history, remove, help, exit")

    while True:
        try:
            command = input("> ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            elif command == "help":
                print("Commands: add, subtract, history, remove, help, exit")

            elif command == "add":
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid number.")
                    continue

                calculation = Add(a, b)
                history.add(calculation)

                print("Result:", calculation.calculate())

            elif command == "subtract":
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid number.")
                    continue

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
                    continue

                for index, calculation in enumerate(calculations, start=1):
                    print(f"{index}. {calculation}")

                try:
                    number = int(input("Enter history number to remove: "))
                    history.remove(number - 1)
                    print("History item removed.")
                except (ValueError, IndexError):
                    print("Invalid history number.")

            else:
                print("Unknown command.")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()