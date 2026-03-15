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

st.title("Student Registration")

name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
password = st.text_input("Password", type="password")

if st.button("Register"):

    if name == "" or email == "" or phone == "" or password == "":
        st.error("All fields are required!")

    else:
        try:
            conn = connect_db()
            cursor = conn.cursor()

            sql = "INSERT INTO students (name, email, phone, password) VALUES (%s, %s, %s, %s)"
            values = (name, email, phone, password)

            cursor.execute(sql, values)
            conn.commit()

            st.success("Registration Successful!")

            cursor.close()
            conn.close()

        except Exception as e:
            st.error(f"Database Error: {e}")
