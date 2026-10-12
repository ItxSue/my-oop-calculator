from unittest.mock import patch

from calculator.cli import main


def test_cli_calculations(capsys):
    commands = [
        "add 5 3",
        "subtract 5 3",
        "multiply 4 2",
        "divide 6 3",
        "history",
        "exit",
    ]

    with patch("builtins.input", side_effect=commands):
        main()

    output = capsys.readouterr().out

    assert "8.0" in output
    assert "2.0" in output
    assert "Goodbye!" in output
    assert "5.0 3.0 = 8.0" in output


def test_cli_errors(capsys):
    commands = [
        "",
        "unknown",
        "add",
        "add 5 abc",
        "divide 6 0",
        "history extra",
        "exit extra",
        "exit",
    ]

    with patch("builtins.input", side_effect=commands):
        main()

    output = capsys.readouterr().out

    assert "Please enter a command." in output
    assert "Unknown command." in output
    assert "Please enter exactly two numbers." in output
    assert "Error:" in output
    assert "Cannot divide by zero" in output
    assert "History does not take any operands." in output
    assert "Exit does not take any operands." in output


def test_cli_empty_history(capsys):
    with patch("builtins.input", side_effect=["history", "exit"]):
        main()

    assert "No history yet." in capsys.readouterr().out


def test_cli_eof(capsys):
    with patch("builtins.input", side_effect=EOFError):
        main()

    assert "Goodbye!" in capsys.readouterr().out


def test_cli_keyboard_interrupt(capsys):
    with patch("builtins.input", side_effect=KeyboardInterrupt):
        main()

    assert "Goodbye!" in capsys.readouterr().out