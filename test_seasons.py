from datetime import date
from seasons import minutes_alive


def test_minutes_alive():
    assert isinstance(minutes_alive(date(2000, 1, 1)), str)
