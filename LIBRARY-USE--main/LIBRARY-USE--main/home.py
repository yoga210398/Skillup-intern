import streamlit as st

st.set_page_config(page_title="Library Management System", layout="centered")

st.title("📚 Library Management System")
st.markdown("---")

st.subheader("Welcome 👋")
st.write(
    """
    This Library Management System is designed for:
    - 📖 Student details viewing  
    - 🔐 Staff login access  
    - 📊 Simple and secure data handling  
    """
)

st.markdown("### Choose your role 👇")

col1, col2 = st.columns(2)

with col1:
    if st.button("👨‍🎓 Student"):
        st.switch_page("student.py")

with col2:
    if st.button("👩‍💼 Staff"):
        st.switch_page("staff.py")

st.markdown("---")
st.caption("Developed using Streamlit | B.Tech IT Project")
