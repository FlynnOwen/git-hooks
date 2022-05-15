from src.add import add


def test_add():
    num1 = 2
    num2 = 3

    assert add(num1, num2) == num1 + num2
