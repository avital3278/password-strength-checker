[![CI](https://github.com/avital3278/password-strength-checker/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/avital3278/password-strength-checker/actions/workflows/ci.yml)

# Password Strength Checker

בודק חוזק סיסמאות מודרני שנכתב בפייתון כחלק מאתגר שרשרת האיכות (CI/CD). הכלי מנתח את הסיסמה ומספק משוב מיידי וציון (Strong, Medium, Weak) בהתאם למורכבות שלה.

## 🛠️ טכנולוגיות וכלי איכות
- **שפה:** Python 3.14
- **ניהול חבילות וסביבה:** [uv](https://astral.sh/uv)
- **Formatter & Linter:** [Ruff](https://github.com/astral-sh/ruff) לשמירה על עיצוב קוד אחיד ונקי.
- **Type Checker:** `ty` / `mypy` לווידוא תקינות טיפוסים סטטית.
- **טסטים אוטומטיים:** [Pytest](https://docs.pytest.org/) עם כיסוי קוד (Coverage) של מעל 93%.
- **אוטומציה:** GitHub Actions (שרשרת CI מלאה הרצה על כל Push ו-PR).

## 🚀 התקנה והרצה מקומית

1. שכפלו את המאגר:
```bash
git clone [https://github.com/avital3278/password-strength-checker.git](https://github.com/avital3278/password-strength-checker.git)
cd password-strength-checker
