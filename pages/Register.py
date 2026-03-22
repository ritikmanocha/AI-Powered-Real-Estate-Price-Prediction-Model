import streamlit as st

st.title("Register Page")

# create user storage
if "users" not in st.session_state:
    st.session_state["users"] = {}

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    if email in st.session_state["users"]:
        st.warning("User already exists")
    else:
        st.session_state["users"][email] = password
        st.success("Registration Successful ✅")
