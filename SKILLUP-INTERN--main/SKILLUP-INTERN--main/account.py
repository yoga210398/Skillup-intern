import streamlit as st
from db import get_connection

def app():
    st.title("Student Account Info")

    student_id = st.number_input("Enter your Student ID", min_value=1, step=1)

    if st.button("Check Account"):
        conn = get_connection()
        cursor = conn.cursor()  # Removed dictionary=True

        cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
        student = cursor.fetchone()

        if student:
            st.write(f"Name: {student['name']}")
            st.write(f"Email: {student['email']}")
            st.write(f"Department: {student['department']}")
            st.write(f"Year: {student['year']}")
        else:
            st.error("Student not found.")

        cursor.close()
        conn.close()
