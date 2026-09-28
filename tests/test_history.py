from calculator.history import History
from calculator.operations import Add


def test_add_to_history():
    history = History()
    calculation = Add(2, 3)

    history.add(calculation)

    assert len(history.get_all()) == 1


def test_clear_history():
    history = History()
    history.add(Add(2, 3))

    history.clear()

    assert history.get_all() == []