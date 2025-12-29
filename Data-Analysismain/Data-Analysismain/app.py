import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Data Analysis Dashboard", layout="wide")

# App title
st.markdown("<h1 style='text-align: center;'>📊 Interactive Data Analysis Dashboard</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ Options")

# Multiple CSV upload
uploaded_files = st.sidebar.file_uploader("Upload CSV Files", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(f"📁 File: {uploaded_file.name}")
        df = pd.read_csv(uploaded_file)

        # Dataset info
        col1, col2 = st.columns(2)
        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])

        st.dataframe(df.head())

        # Statistical summary
        st.subheader("📈 Statistical Summary")
        st.write(df.describe())

        # Numeric columns
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

        if len(numeric_cols) > 0:
            st.sidebar.subheader(f"📊 Visualization Settings for {uploaded_file.name}")

            column = st.sidebar.selectbox(f"Select Column for {uploaded_file.name}", numeric_cols, key=uploaded_file.name)
            chart_type = st.sidebar.selectbox(
                f"Select Chart Type for {uploaded_file.name}",
                ["Histogram", "Bar Chart", "Line Chart"],
                key=uploaded_file.name+"_chart"
            )

            st.subheader(f"📉 Data Visualization for {uploaded_file.name}")

            plt.figure(figsize=(8,5))

            if chart_type == "Histogram":
                plt.hist(df[column], bins=10, color='skyblue', edgecolor='black')
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.title(f"Histogram of {column}")

            elif chart_type == "Bar Chart":
                plt.bar(df.index[:10], df[column][:10], color='orange')
                plt.xlabel("Index")
                plt.ylabel(column)
                plt.title(f"Bar Chart of {column} (first 10 rows)")

            elif chart_type == "Line Chart":
                plt.plot(df[column], marker='o', linestyle='-', color='green')
                plt.xlabel("Index")
                plt.ylabel(column)
                plt.title(f"Line Chart of {column}")

            st.pyplot(plt)

        else:
            st.warning("⚠️ No numeric columns found in this file!")

else:
    st.info("📁 Please upload at least one CSV file to start analysis")
