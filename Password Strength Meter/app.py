import streamlit as st
import re

# Custom CSS with Tailwind-like classes
st.markdown("""
<style>
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(45deg, #FF512F, #DD2476);
        padding: 20px;
    }
    
    /* Password input container */
    .password-container {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Result text styling */
    .strong-password {
        color: #10B981;
        font-weight: bold;
    }
    .medium-password {
        color: #F59E0B;
        font-weight: bold;
    }
    .weak-password {
        color: #EF4444;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar setup
st.sidebar.title("Password Checker Settings")
st.sidebar.markdown("---")

# Minimum length setting in sidebar
min_length = st.sidebar.slider("Minimum Password Length", 8, 20, 8)

# Special character requirement
require_special = st.sidebar.checkbox("Require Special Characters", value=True)
require_numbers = st.sidebar.checkbox("Require Numbers", value=True)
require_uppercase = st.sidebar.checkbox("Require Uppercase", value=True)

# Main content
st.title("Password Strength Checker")
st.markdown('<div class="password-container">', unsafe_allow_html=True)

# Password input
password = st.text_input("Enter your password", type="password")

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= min_length:
        score += 1
    else:
        feedback.append(f"Password should be at least {min_length} characters long")
    
    # Special character check
    if require_special and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    elif require_special:
        feedback.append("Add special characters")
    
    # Number check
    if require_numbers and re.search(r"\d", password):
        score += 1
    elif require_numbers:
        feedback.append("Add numbers")
    
    # Uppercase check
    if require_uppercase and re.search(r"[A-Z]", password):
        score += 1
    elif require_uppercase:
        feedback.append("Add uppercase letters")
    
    return score, feedback

if password:
    strength, feedback = check_password_strength(password)
    
    # Display strength
    if strength >= 4:
        st.markdown('<p class="strong-password">Strong Password! ✅</p>', unsafe_allow_html=True)
    elif strength >= 2:
        st.markdown('<p class="medium-password">Medium Password! ⚠️</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="weak-password">Weak Password! ❌</p>', unsafe_allow_html=True)
    
    # Display feedback
    if feedback:
        st.markdown("### Improvements needed:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")

st.markdown('</div>', unsafe_allow_html=True)