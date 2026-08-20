from app import multiplicacao, soma, subtracao


def test_soma():
    assert soma(2, 3) == 5


def test_subtracao():
    assert subtracao(5, 3) == 2


def test_multiplicacao():
    assert multiplicacao(4, 3) == 12
