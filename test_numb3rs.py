from numb3rs import validate


def test_valid():
    assert validate("255.255.255.255") is True
    assert validate("192.168.1.1") is True
    assert validate("8.8.8.8") is True
    assert validate("0.0.0.0") is True


def test_invalid_range():
    assert validate("256.0.0.1") is False
    assert validate("192.168.256.1") is False
    assert validate("999.999.999.999") is False


def test_invalid_format():
    assert validate("192.168.1") is False
    assert validate("192.168.1.1.1") is False
    assert validate("cat") is False
    assert validate("192.168.one.1") is False
    assert validate("000.001.010.100") is False
