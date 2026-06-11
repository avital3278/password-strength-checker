import getpass


def check_password_strength(password: str) -> dict[str, str | list[str]]:
    feedback: list[str] = []

    if len(password) < 8:
        feedback.append("הסיסמה חייבת להיות באורך של 8 תווים לפחות.")

    if not any(char.isupper() for char in password):
        feedback.append("הסיסמה חייבת להכיל לפחות אות גדולה אחת (A-Z).")

    if not any(char.islower() for char in password):
        feedback.append("הסיסמה חייבת להכיל לפחות אות קטנה אחת (a-z).")

    if not any(char.isdigit() for char in password):
        feedback.append("הסיסמה חייבת להכיל לפחות מספר אחד (0-9).")

    special_characters = '!@#$%^&*(),.?":{}|<>'
    if not any(char in special_characters for char in password):
        feedback.append("הסיסמה חייבת להכיל לפחות תו מיוחד אחד (כמו !, @, #, $).")

    if len(feedback) == 0:
        strength = "Strong"
    elif len(feedback) <= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    return {"strength": strength, "feedback": feedback}


if __name__ == "__main__":  # pragma: no cover
    user_password = getpass.getpass("Enter a password to check its strength: ")
    result = check_password_strength(user_password)
    print(f"Password Strength Result: {result}")
