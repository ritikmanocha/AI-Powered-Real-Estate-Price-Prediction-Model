import streamlit as st

st.title("Login Page")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if "users" in st.session_state and email in st.session_state["users"]:
        if st.session_state["users"][email] == password:
            st.session_state["logged_in"] = True
            st.success("Login Successful ✅")
        else:
            st.error("Wrong Password ❌")
    else:
        st.error("User not found ❌")
