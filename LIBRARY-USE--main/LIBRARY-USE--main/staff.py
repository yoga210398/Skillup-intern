import streamlit as st
import pandas as pd
import os

st.title("🔐 Staff Login")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "staff.csv")

df = pd.read_csv(csv_path)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = df[(df["Username"] == username) & (df["Password"] == password)]
    if not user.empty:
        st.success(f"Welcome {user.iloc[0]['Name']} 👋")
    else:
        st.error("Invalid username or password ❌")
