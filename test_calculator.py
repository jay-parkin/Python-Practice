from calculator import add

def test_basic():
    assert "hello" == "hello"


def test_add():
    assert add(2, 3) == 6
    assert add(2, 3) == 5
    assert add(2, 3) == 6
    assert add(2, 3) == 5
    assert add(2, 3) == 5

