import builtins
import runpy

from calculator.main import main


def run_calculator(monkeypatch, inputs):
    responses = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(responses))
    main()


def test_main_commands(monkeypatch, capsys):
    run_calculator(
        monkeypatch,
        [
            "help",
            "history",
            "remove",
            "blah",
            "add",
            "2",
            "3",
            "subtract",
            "10",
            "4",
            "history",
            "remove",
            "1",
            "history",
            "exit",
        ],
    )

    output = capsys.readouterr().out

    assert "Calculator started." in output
    assert "No history yet." in output
    assert "No history to remove." in output
    assert "Unknown command." in output
    assert "Result: 5.0" in output
    assert "Result: 6.0" in output
    assert "Add: 2.0 + 3.0 = 5.0" in output
    assert "Subtract: 10.0 - 4.0 = 6.0" in output
    assert "History item removed." in output
    assert "Goodbye!" in output


def test_invalid_add(monkeypatch, capsys):
    run_calculator(
        monkeypatch,
        ["add", "abc", "exit"],
    )

    output = capsys.readouterr().out
    assert "Invalid number." in output


def test_invalid_subtract(monkeypatch, capsys):
    run_calculator(
        monkeypatch,
        ["subtract", "abc", "exit"],
    )

    output = capsys.readouterr().out
    assert "Invalid number." in output


def test_invalid_remove(monkeypatch, capsys):
    run_calculator(
        monkeypatch,
        ["add", "2", "3", "remove", "99", "exit"],
    )

    output = capsys.readouterr().out
    assert "Invalid history number." in output


def test_keyboard_interrupt(monkeypatch, capsys):
    def raise_interrupt(_):
        raise KeyboardInterrupt

    monkeypatch.setattr(builtins, "input", raise_interrupt)

    main()

    output = capsys.readouterr().out
    assert "Goodbye!" in output


def test_eof_error(monkeypatch, capsys):
    def raise_eof(_):
        raise EOFError

    monkeypatch.setattr(builtins, "input", raise_eof)

    main()

    output = capsys.readouterr().out
    assert "Goodbye!" in output


def test_main_module(monkeypatch):
    responses = iter(["exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(responses))

    runpy.run_module("calculator.main", run_name="__main__")