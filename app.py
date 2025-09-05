import streamlit as st

# ----------------- DARK / LIGHT MODE -----------------
# Initialize theme in session state
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Place toggle button in top-right corner
col1, col2 = st.columns([9, 1])
with col2:
    if st.button("🌙" if st.session_state.theme == "light" else "☀️"):
        st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Apply CSS for themes
if st.session_state.theme == "dark":
    st.markdown(
        """
        <style>
        .stApp { 
            background-color: #121212; 
            color: #ffffff; 
        }
        .stButton>button {
            background-color: #333333;
            color: #ffffff;
            border-radius: 8px;
        }
        .stSelectbox, .stTextInput, .stMultiSelect {
            background-color: #1e1e1e !important;
            color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .stApp { 
            background-color: #ffffff; 
            color: #000000; 
        }
        .stButton>button {
            background-color: #f0f0f0;
            color: #000000;
            border-radius: 8px;
        }
        .stSelectbox, .stTextInput, .stMultiSelect {
            background-color: #ffffff !important;
            color: #000000 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# ----------------- END DARK / LIGHT MODE -----------------
