from main import check_password_strength


# 1
def test_strong_password():
    result = check_password_strength("Strong123!")
    assert result["strength"] == "Strong"
    assert len(result["feedback"]) == 0


# 2
def test_medium_password_too_short():
    result = check_password_strength("Abc123!")
    assert result["strength"] == "Medium"
    assert "הסיסמה חייבת להיות באורך של 8 תווים לפחות." in result["feedback"]


# 3
def test_medium_password_no_special_char():
    result = check_password_strength("Password123")
    assert result["strength"] == "Medium"
    assert (
        "הסיסמה חייבת להכיל לפחות תו מיוחד אחד (כמו !, @, #, $)." in result["feedback"]
    )


# 4
def test_weak_password_only_lowercase():
    result = check_password_strength("pass")
    assert result["strength"] == "Weak"
    assert len(result["feedback"]) == 4


# 5
def test_empty_password():
    result = check_password_strength("")
    assert result["strength"] == "Weak"
    assert len(result["feedback"]) == 5
