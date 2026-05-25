import streamlit as st
import re

# ---------------- Session State ----------------

if "history" not in st.session_state:
    st.session_state.history=[]


# ---------------- OOP CLASS ----------------

class PasswordChecker:

    def __init__(self,password):
        self.password=password
        self.score=0
        self.suggestions=[]

    def check_length(self):
        if len(self.password)>=8:
            self.score+=20
        else:
            self.suggestions.append("❌ Password should be at least 8 characters")

    def check_uppercase(self):
        if any(char.isupper() for char in self.password):
            self.score+=20
        else:
            self.suggestions.append("❌ Add uppercase letter")

    def check_lowercase(self):
        if any(char.islower() for char in self.password):
            self.score+=20
        else:
            self.suggestions.append("❌ Add lowercase letter")

    def check_number(self):
        if any(char.isdigit() for char in self.password):
            self.score+=20
        else:
            self.suggestions.append("❌ Add a number")

    def check_special(self):
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]",self.password):
            self.score+=20
        else:
            self.suggestions.append("❌ Add special character")

    def common_password(self):

        common=[
            "123456",
            "password",
            "admin",
            "qwerty",
            "abc123"
        ]

        if self.password.lower() in common:
            self.score=0
            self.suggestions.append("⚠ Common password detected")

    def calculate_strength(self):

        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_number()
        self.check_special()
        self.common_password()

        return self.score


# ---------------- SIDEBAR ----------------

st.sidebar.header("Password Rules 🔐")

st.sidebar.write("✔ Minimum 8 characters")
st.sidebar.write("✔ Uppercase")
st.sidebar.write("✔ Lowercase")
st.sidebar.write("✔ Number")
st.sidebar.write("✔ Special Character")


# ---------------- UI ----------------

st.title("🔐 Password Strength Checker")

show=st.checkbox("Show Password")


if show:
    password=st.text_input("Enter Password")
    confirm=st.text_input("Confirm Password")

else:
    password=st.text_input(
        "Enter Password",
        type="password"
    )

    confirm=st.text_input(
        "Confirm Password",
        type="password"
    )


analyze=st.button("Analyze Password")


# ---------------- LOGIC ----------------

if analyze:

    if password!=confirm:

        st.error("Passwords do not match")

    else:

        checker=PasswordChecker(password)

        score=checker.calculate_strength()

        st.progress(score)

        st.write(f"Security Score: {score}/100")

        if score<=30:
            strength="Weak ❌"

        elif score<=60:
            strength="Medium ⚠"

        elif score<=80:
            strength="Strong ✅"

        else:
            strength="Very Strong 🚀"

        st.success(f"Password Strength: {strength}")

        st.subheader("Suggestions")

        if checker.suggestions:

            for item in checker.suggestions:
                st.write(item)

        else:
            st.write("Perfect Password 🎉")

        st.session_state.history.append(strength)


# ---------------- HISTORY ----------------

with st.expander("View History"):

    if st.session_state.history:

        for item in st.session_state.history:
            st.write(item)

    else:
        st.write("No history yet")


clear=st.button("Clear History")

if clear:
    st.session_state.history=[]
    st.rerun()
