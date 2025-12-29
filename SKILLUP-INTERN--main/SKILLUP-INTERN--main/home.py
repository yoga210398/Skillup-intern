import streamlit as st

def app():
    # Page title with custom styling
    st.markdown("""
        <h1 style='text-align: center; color: #1E90FF; font-family: "Trebuchet MS";'>
        📚 Welcome to the Library Management System
        </h1>
        """, unsafe_allow_html=True)

    # Subtitle
    st.markdown("""
        <h3 style='text-align: center; color: #555555; font-family: "Georgia";'>
        Your gateway to knowledge, research, and exploration!
        </h3>
        """, unsafe_allow_html=True)

    # Divider
    st.markdown("---")

    # Two-column layout for text + image
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <h2 style='color: #1E90FF;'>Why Visit Our Library?</h2>
            <ul style='font-size:18px;'>
                <li>Access hundreds of books in various categories 📖</li>
                <li>Keep track of borrowed books and due dates ⏰</li>
                <li>Explore top trending books and recommendations 🌟</li>
                <li>Effortless account management for students and staff 👥</li>
            </ul>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=800&q=80",
            width=500,  # Updated parameter instead of deprecated use_column_width
            caption="Discover a world of books"
        )

    # Another section
    st.markdown("---")
    st.markdown
