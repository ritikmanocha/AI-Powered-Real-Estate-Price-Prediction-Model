import streamlit as st
import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

st.title("Student Login")

email_input = st.text_input("Email")
pass_input = st.text_input("Password", type="password")

if st.button("Login"):

    if email_input == "" or pass_input == "":
        st.error("All fields are required")

    else:
        try:
            conn = connect_db()
            cursor = conn.cursor()

            sql = "SELECT * FROM students WHERE email=%s AND password=%s"
            cursor.execute(sql, (email_input, pass_input))

            result = cursor.fetchone()

            if result:
                st.success(f"Welcome {result[1]}")
                st.session_state["logged_in"] = True
            else:
                st.error("Invalid email or password")

            cursor.close()
            conn.close()

        except Exception as e:
            st.error(f"Database Error: {e}")
