import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5


def test_overflow():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3


def test_underflow():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
