from plates import is_valid


def test_length():
    assert is_valid("CS") is True
    assert is_valid("CS50") is True
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False


def test_first_two_letters():
    assert is_valid("CS50") is True
    assert is_valid("22CS") is False
    assert is_valid("C1") is False


def test_first_number():
    assert is_valid("CS05") is False
    assert is_valid("CS50") is True


def test_numbers_middle():
    assert is_valid("CS50P") is False
    assert is_valid("AAA22A") is False


def test_punctuation():
    assert is_valid("CS.50") is False
    assert is_valid("CS,50") is False
    assert is_valid("CS 50") is False
    assert is_valid("CS-50") is False


def test_empty():
    assert is_valid("") is False
