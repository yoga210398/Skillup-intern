import streamlit as st
import pandas as pd
import os

st.title("📚 Student Details")

# Safe CSV path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "students.csv")

df = pd.read_csv(csv_path)

st.subheader("Student List")
st.dataframe(df)
