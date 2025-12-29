import streamlit as st
from streamlit_option_menu import option_menu

import about, account, home, StaffLogin, StudentLogin

st.set_page_config(page_title="Library Management System")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="Library Management System",
                options=["Home", "StudentLogin", "StaffLogin", "Account", "About"],
                icons=["house", "person", "person-check", "person-circle", "info-circle"],
                menu_icon="cast",
                default_index=0
            )

        if app == "Home":
            home.app()
        elif app == "StudentLogin":
            StudentLogin.app()
        elif app == "StaffLogin":
            StaffLogin.app()
        elif app == "Account":
            account.app()
        elif app == "About":
            about.app()

# Run the app
app = MultiApp()
app.run()
