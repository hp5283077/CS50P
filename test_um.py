from um import count


def test_single():
    assert count("um") == 1


def test_multiple():
    assert count("um, thanks, um...") == 2


def test_case():
    assert count("Um, thanks, uM.") == 2


def test_not_word():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0


def test_mixed():
    assert count("Um? um! yummy album UM") == 3
