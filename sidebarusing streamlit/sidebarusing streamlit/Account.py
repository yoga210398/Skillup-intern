import streamlit as st
from db import get_connection
from psycopg2.extras import RealDictCursor

def app():
    st.title("Student Account Info")

    student_id = st.number_input("Enter your Student ID", min_value=1, step=1)

    if st.button("Check Account"):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s",
            (student_id,)
        )
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
import streamlit as st

def app():
    st.title("Library Management System")
    st.write("""
    This Library Management System is built using *Python, Streamlit, and PostgreSQL*.

    Features:
    - Student Login
    - Staff Login
    - View Books
    - Manage Account
    """)