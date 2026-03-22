import streamlit as st

st.set_page_config(page_title="ML App", layout="centered")

st.title("🏠 AI-Powered ML Project")

# ---------- Initialize session variables ----------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "paid" not in st.session_state:
    st.session_state["paid"] = False

# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go to",
    ["Home", "Register", "Login", "Payment", "ML Model"]
)

# ---------- HOME ----------
if menu == "Home":
    st.subheader("Welcome 👋")
    st.write("This is an AI-powered ML application.")

# ---------- REGISTER ----------
elif menu == "Register":
    st.switch_page("pages/Register.py")

# ---------- LOGIN ----------
elif menu == "Login":
    st.switch_page("pages/Login.py")

# ---------- PAYMENT ----------
elif menu == "Payment":
    if not st.session_state["logged_in"]:
        st.warning("Please login first 🔐")
    else:
        st.switch_page("pages/Payment.py")

# ---------- ML MODEL ----------
elif menu == "ML Model":
    if not st.session_state["logged_in"]:
        st.warning("Please login first 🔐")
    elif not st.session_state["paid"]:
        st.warning("Please complete payment first 💳")
    else:
        st.switch_page("pages/ML_model.py")
