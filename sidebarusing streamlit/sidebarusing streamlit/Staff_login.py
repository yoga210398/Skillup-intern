import streamlit as st
from db import get_connection
from psycopg2.extras import RealDictCursor

def app():
    st.title("Staff Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            conn = get_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)

            query = """
                SELECT name, role
                FROM staff
                WHERE email = %s AND password = %s
            """
            cursor.execute(query, (email, password))
            staff = cursor.fetchone()

            if staff:
                st.success(f"Welcome, {staff['name']}! Role: {staff['role']}")
            else:
                st.error("Invalid email or password")

        except Exception as e:
            st.error("Database error occurred")
            st.write(e)   # shows real error for debugging

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()