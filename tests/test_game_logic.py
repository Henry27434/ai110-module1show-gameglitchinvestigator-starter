from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


# --- Starter tests (fixed to unpack tuple return value) ---

def test_winning_guess():
    # FIX: check_guess returns a tuple (outcome, message), not just a string.
    # Original test did `assert result == "Win"` which always failed.
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- New tests targeting fixed bugs ---

def test_hint_too_high_says_go_lower():
    """When guess is too high, the message should tell the player to go LOWER."""
    # Bug was: "Too High" showed "📈 Go HIGHER!" — the wrong direction entirely.
    _, message = check_guess(60, 50)
    assert "LOWER" in message


def test_hint_too_low_says_go_higher():
    """When guess is too low, the message should tell the player to go HIGHER."""
    # Bug was: "Too Low" showed "📉 Go LOWER!" — also wrong direction.
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_wrong_guess_always_decreases_score():
    """Wrong guesses (Too High) should always subtract points, never add them."""
    # Bug was: on even attempt_numbers, Too High added +5 points as a reward.
    score_even_attempt = update_score(100, "Too High", 2)
    score_odd_attempt = update_score(100, "Too High", 3)
    assert score_even_attempt < 100, "Score should decrease on even attempts too"
    assert score_odd_attempt < 100


def test_too_low_decreases_score():
    """Too Low guesses should also subtract points."""
    score = update_score(100, "Too Low", 1)
    assert score < 100


def test_win_increases_score():
    """Winning should award points."""
    score = update_score(0, "Win", 1)
    assert score > 0


def test_check_guess_with_string_secret_does_not_break():
    """The fixed check_guess should handle a string secret gracefully by converting to int."""
    # Bug was: app.py passed str(secret) on even attempts, causing string comparison.
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"


def test_hard_difficulty_range_is_hardest():
    """Hard mode should have a larger range than Normal, making it harder."""
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, "Hard difficulty should cover a wider range than Normal"


def test_easy_difficulty_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_parse_guess_valid_int():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None


def test_parse_guess_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert "not a number" in err.lower()


def test_parse_guess_decimal_truncates():
    """Decimal inputs should be accepted and truncated to int."""
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7