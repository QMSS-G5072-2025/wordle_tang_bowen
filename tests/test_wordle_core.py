from wordle_bt2683.wordle import validate_guess, check_guess


def test_validate_guess():
    assert validate_guess("crane") is True
    assert validate_guess("CRANE") is False
    assert validate_guess("abcd") is False
    assert validate_guess("ab1de") is False
    assert validate_guess(None) is False


def test_check_guess_basic():
    assert check_guess("crane", "crane") == [
        ("c", "green"), ("r", "green"), ("a", "green"), ("n", "green"), ("e", "green")
    ]

    assert check_guess("crane", "react") == [
        ("r", "yellow"), ("e", "yellow"), ("a", "green"), ("c", "yellow"), ("t", "gray")
    ]

    assert check_guess("crane", "toolong") == []
