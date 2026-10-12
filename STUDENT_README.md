
# CLI Calculator — IS218

## Project Overview

This project is a Python command-line calculator that performs addition, subtraction, multiplication, and division. It uses Object-Oriented Programming (OOP) and design patterns to organize calculations, commands, and history.

## Setup Instructions

This project requires Python 3.12 or newer.

Create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For Windows PowerShell, activate the virtual environment using:

```powershell
.venv\Scripts\Activate.ps1
```

## Running the Calculator

Start the calculator using:

```bash
python -m calculator
```

Example commands and output:

```text
> add 5 3
8.0
> subtract 5 3
2.0
> multiply 4 2
8.0
> divide 6 3
2.0
> history
5.0 3.0 = 8.0
5.0 3.0 = 2.0
4.0 2.0 = 8.0
6.0 3.0 = 2.0
> exit
Goodbye!
```

The calculator accepts decimal and negative numbers. It also handles invalid inputs and division by zero without stopping.

Only successful calculations are saved in history.

## Testing

Run the tests using:

```bash
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

The local test run passed 25 tests with 100% line coverage.

The entry-point code in `__main__.py` uses `# pragma: no cover` because its purpose is only to start the CLI. The calculator's actual behavior is tested separately.

## Object-Oriented Programming Concepts

### Encapsulation

The `Calculation` class stores two numbers and their selected operation. The `HistoryCommand` class returns a copy of the history list so changes to the returned list do not affect the stored history.

### Abstraction

The abstract `Calculation` class requires subclasses to provide an `execute()` method.

### Inheritance

`ArithmeticCalculation` inherits from `Calculation` and implements the required `execute()` method.

### Polymorphism

Different calculations can be executed through the same `execute()` method. The command can work with calculations that follow this interface.

### Composition

`CalculateCommand` holds a calculation object, and `ArithmeticCalculation` holds a selected operation function.

## SOLID Principles

### Single Responsibility Principle

Each class has a specific responsibility. `Operations` performs arithmetic, `ArithmeticCalculation` executes calculations, and `CalculateCommand` coordinates execution and history.

### Open/Closed Principle

A new arithmetic operation can be added without changing the calculation execution logic. The new operation can be registered in the CLI dictionary.

### Liskov Substitution Principle

Concrete calculations should follow the same contract as the abstract `Calculation` class by returning a numeric result or raising an appropriate error.

### Interface Segregation Principle

The calculation interface remains small because subclasses only need to implement `execute()`.

### Dependency Inversion Principle

`CalculateCommand` receives a calculation object rather than hard-coding a specific arithmetic operation. The calculation also receives its operation function.

## Design Patterns

### Factory Pattern

The `create()` class method in `ArithmeticCalculation` creates calculation objects from two numbers and a selected operation.

### Command Pattern

`CalculateCommand` executes calculations and adds successful results to history. `HistoryCommand` retrieves a copy of the stored history.

### Strategy Pattern

The CLI uses a dictionary to select an arithmetic function based on the user's command. The calculation then executes that selected function.

## Python Method Types

**Static method:** The arithmetic methods in `Operations` use `@staticmethod` because they do not need object or class state.

**Class method:** The `create()` method uses `@classmethod` and `cls` to construct an object.

**Instance method:** The `execute()` method uses `self` to access the calculation's stored values and operation.

## GitHub Actions

GitHub Actions automatically runs the test suite on pushes and pull requests. The workflow installs the dependencies and requires 100% line coverage.

Successful GitHub Actions run:

https://github.com/ItxSue/my-oop-calculator/actions/runs/38189706228

## Conclusion

I reused parts of my earlier calculator and added new classes, commands, and tests. Separating arithmetic, calculations, history, and user input makes the project easier to understand, test, and extend.
