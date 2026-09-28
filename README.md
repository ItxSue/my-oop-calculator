# OOP Calculator

This project is a command-line calculator built in Python using object-oriented programming concepts.

## Features

- Add two numbers
- Subtract two numbers
- View calculation history
- Remove items from calculation history
- Handle invalid input without crashing
- Run automated tests with pytest
- Maintain 100% line and branch coverage

## Run the Calculator

```bash
python -m calculator.main

## Reflection

I would create a Multiply class by creating the same structure as Add and Subtract. I would also add multiply to the help menu to make sure the multiplication works correctly. The History class does not need multiplication-specific logic since it stores calculation objects without it knowing what operation each object performs. 

Email and text-message notifcation objects could share a common contract which might require to send() method. Each type of notifcation could implement send() differently while they are in the same interface.

The design knowlege transers to another programming language is inheritance, polymorphism, encapsulation, abstraction, and separating responsibilities between classes. If I did use another language, I would still need to learn that language syntax, and how it handles classes and interfaces. 