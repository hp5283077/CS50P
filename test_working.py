import pytest
from working import convert


def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_minutes():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("12:15 AM to 12:45 PM") == "00:15 to 12:45"


def test_invalid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("cat")
