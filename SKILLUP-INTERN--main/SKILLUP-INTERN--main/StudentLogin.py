import streamlit as st
import pandas as pd
from db import get_connection

def student_dashboard(student_id):
    st.subheader("📊 Student Dashboard")
    conn = get_connection()

    query = """
    SELECT b.title
    FROM borrow_history bh
    JOIN books b ON bh.book_id = b.book_id
    WHERE bh.user_type='student' AND bh.user_id=?
    """

    df = pd.read_sql(query, conn, params=(student_id,))
    conn.close()

    if not df.empty:
        st.subheader("📚 Borrowed Books")
        book_counts = df['title'].value_counts().reset_index()
        book_counts.columns = ["Book Title", "Count"]
        st.dataframe(book_counts)
        st.subheader("📊 Borrowed Books Chart")
        st.bar_chart(book_counts.set_index("Book Title"))
    else:
        st.info("No borrowed books found.")

def app():
    st.title("🎓 Student Login")

    email = st.text_input("Email", key="student_email")
    password = st.text_input("Password", type="password", key="student_password")

    if st.button("Login", key="student_login"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students WHERE email=? AND password=?", (email, password))
        student = cursor.fetchone()

        if student:
            st.success(f"Welcome, {student['name']} 👋")
            student_dashboard(student['student_id'])
        else:
            st.error("Invalid email or password")

        cursor.close()
        conn.close()
