import streamlit as st
import re
import random
import string

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
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "green", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "orange", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", "red", feedback

def generate_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit App UI
st.title("🔒 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    strength_msg, color, feedback = check_password_strength(password)
    st.markdown(f"<span style='color:{color}; font-size:18px;'>{strength_msg}</span>", unsafe_allow_html=True)
    for fb in feedback:
        st.write(fb)

if st.button("🔑 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text(f"Suggested Password: {strong_password}")

# Run the app using: streamlit run app.py
