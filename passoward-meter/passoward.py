import re
import random
import string
import streamlit as st

# Function to generate a strong password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Common Password Check
    common_passwords = ["password", "123456", "qwerty", "password123", "letmein"]
    if password.lower() in common_passwords:
        feedback.append("❌ Password is too common. Choose a more secure one.")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        feedback.append(f"🔹 Suggested Strong Password: {generate_strong_password()}")
        return "❌ Weak Password - Improve it using the suggestions above.", feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if st.button("Check Passoward Strength"):
    if password:
        strength, suggestions = check_password_strength(password)
        st.subheader(strength)
        for tip in suggestions:
            st.write(tip)
    else:
        st.warning("⚠️ Please enter a password!")

if st.button("Generate Strong Password"):
    st.info(f"🔑 Suggested Password: `{generate_strong_password()}`")