[![CI Pipeline](https://github.com/avital3278/password-strength-checker/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/avital3278/password-strength-checker/actions/workflows/ci.yml)
[![Coverage Status](https://img.shields.io/badge/coverage-93%25-brightgreen.svg)]()

# 🔐 Password Strength Analyzer

A robust, Python-based CLI tool designed to evaluate password complexity and provide immediate, user-friendly feedback. Built as part of an advanced CI/CD engineering challenge, this project demonstrates industry-standard quality assurance workflows.

---

## 🎯 How It Works

The analyzer evaluates any given password against multiple security criteria and assigns a strength rating from `Super Weak` to `Very Strong`.

**The algorithm checks for:**
* Minimum length of 8 characters
* Presence of lowercase letters (a-z)
* Presence of uppercase letters (A-Z)
* Presence of numerical digits (0-9)
* Presence of special characters (!@#$%^&*)

Based on these checks, the tool calculates a comprehensive score and returns an intuitive visual rating.

---

## 🏗️ Tech Stack & QA Automation

This project is built with modern Python development tools to ensure code reliability and maintainability:

* **Language:** Python 3.14
* **Dependency Management:** `uv` (Fast Python package installer)
* **Static Analysis:** `Ruff` (Lightning-fast linter and code formatter)
* **Type Checking:** `ty` / `mypy` (Strict static type validation)
* **Testing Framework:** `pytest` with `pytest-cov` (Maintaining >93% code coverage)
* **CI/CD:** Automated GitHub Actions pipeline running on every push.

---

## 🚀 Getting Started

Follow these steps to clone the repository, install dependencies, run the application, and execute the test suite locally:

```bash
# 1. Clone & Install
git clone [https://github.com/avital3278/password-strength-checker.git](https://github.com/avital3278/password-strength-checker.git)
cd password-strength-checker
uv sync --dev

# 2. Run the Application
python main.py

# 3. Run the Quality Pipeline (Local CI)
uv run ruff check .
uv run ty check
uv run pytest --cov --cov-fail-under=80
```
