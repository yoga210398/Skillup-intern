import streamlit as st
from db import get_connection

def app():
    conn = get_connection()
    cursor = conn.cursor()   # ✅ FIXED

    # Show books available in the library
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()

    st.subheader("Available Books")
    if books:
        st.table(books)
    else:
        st.write("No books available.")

    cursor.close()
    conn.close()
import streamlit as st
from db import get_connection

def app():
    conn = get_connection()
    cursor = conn.cursor()   # ✅ FIXED

    # Show books available in the library
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()

    st.subheader("Available Books")
    if books:
        st.table(books)
    else:
        st.write("No books available.")

    cursor.close()
    conn.close()