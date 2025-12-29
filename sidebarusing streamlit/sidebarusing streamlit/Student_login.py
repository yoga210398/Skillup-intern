import streamlit as st
from db import get_connection
from psycopg2.extras import RealDictCursor

def app():
    st.title("Student_Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        query = "SELECT * FROM library_db WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        library_db = cursor.fetchone()

        if library_db:
            st.success(f"Welcome, {library_db['name']}!")
        else:
            st.error("Invalid email or password")

        cursor.close()
        conn.close()