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
import streamlit as st
from streamlit_option_menu import option_menu

import Home, Student_login, Staff_login, Account, About

st.set_page_config(page_title="Library Management System")

class MultiApp:
    def _init_(self):   # ✅ FIXED
        self.apps = []

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="Library Management System",
                options=["Home", "Student_Login", "Staff_Login", "Account", "About"],
                icons=["house", "person", "person-check", "person-circle", "info-circle"],
                menu_icon="cast",
                default_index=0
            )

        if app == "Home":
            Home.app()
        elif app == "Student_Login":
            Student_login.app()
        elif app == "Staff_Login":
            Staff_login.app()
        elif app == "Account":
            Account.app()
        elif app == "About":
            About.app()

app = MultiApp()
app.run()