# 🔐 Streamlit Password Strength Checker

A Password Strength Checker built using **Python**, **Streamlit**, and **Object-Oriented Programming (OOP)** that analyzes password security and provides smart suggestions.

## 🚀 Features

- 🔒 Hidden password input
- 🔁 Confirm password field
- 👁 Show / Hide password option
- 📊 Password strength score (0–100)
- 📈 Progress bar visualization
- ⚠ Detect weak/common passwords
- 💡 Smart suggestions to improve password
- 🧠 OOP implementation using `PasswordChecker` class
- 📜 Password analysis history
- 🗑 Clear history functionality
- 📋 Sidebar password rules

---

## 🛠 Tech Stack

- Python
- Streamlit
- OOP (Classes & Methods)
- Regex (`re`)
- Session State

---

## 📂 Project Structure

```text
streamlit-password-checker/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔍 Password Rules

A strong password should contain:

✔ Minimum 8 characters  
✔ Uppercase letter  
✔ Lowercase letter  
✔ Number  
✔ Special character

---

## 🧠 OOP Design

The project uses a class:

```python
class PasswordChecker
```

Methods include:

- `check_length()`
- `check_uppercase()`
- `check_lowercase()`
- `check_number()`
- `check_special()`
- `common_password()`
- `calculate_strength()`

This keeps the code modular and reusable.

---

## ▶ Run Locally

Clone repository:

```bash
git clone YOUR_REPOSITORY_LINK
```

Move into project:

```bash
cd streamlit-password-checker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app:

```bash
streamlit run app.py
```

---

## 📦 requirements.txt

```text
streamlit
```

---

## 🚀 Live Demo

👉 Add Streamlit deployment link here

Example:

https://your-password-checker.streamlit.app

---

## 📸 Screenshots

[Image](image.png)


## ✨ Future Improvements

- Password entropy calculation
- Real breach detection API
- Password generator
- Export analysis report
- Dark mode support

---

## 👨‍💻 Author

Subhi Sharma
B.Tech CSE (AI & ML)