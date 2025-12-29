import streamlit as st

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Library Management System")
st.markdown("---")

st.subheader("Select Page 👇")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("pages/01_Home.py")

with col2:
    if st.button("👨‍🎓 Student"):
        st.switch_page("pages/02_Student.py")

with col3:
    if st.button("👩‍💼 Staff"):
        st.switch_page("pages/03_Staff.py")

st.markdown("---")
st.caption("B.Tech IT | Streamlit Project")
