import streamlit as st
import pandas as pd
from db import get_connection

def staff_dashboard(staff_id):
    st.subheader("👩‍🏫 Staff Dashboard")
    conn = get_connection()

    query = """
    SELECT b.title
    FROM borrow_history bh
    JOIN books b ON bh.book_id = b.book_id
    WHERE bh.user_type='staff' AND bh.user_id=?
    """

    df = pd.read_sql(query, conn, params=(staff_id,))
    conn.close()

    if not df.empty:
        st.subheader("📚 Books Issued")
        book_counts = df['title'].value_counts().reset_index()
        book_counts.columns = ["Book Title", "Count"]
        st.dataframe(book_counts)
        st.subheader("📊 Books Issued Chart")
        st.bar_chart(book_counts.set_index("Book Title"))
    else:
        st.info("No records found.")

def app():
    st.title("👨‍💼 Staff Login")

    email = st.text_input("Email", key="staff_email")
    password = st.text_input("Password", type="password", key="staff_password")

    if st.button("Login", key="staff_login"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM staff WHERE email=? AND password=?", (email, password))
        staff = cursor.fetchone()

        if staff:
            st.success(f"Welcome {staff['name']} ({staff['role']})")
            staff_dashboard(staff['staff_id'])
        else:
            st.error("Invalid credentials")

        cursor.close()
        conn.close()
