import pandas as pd
import streamlit as st
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Affiliate Offers Dashboard", layout="wide")

# ----------------------------
# Heading
# ----------------------------
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="
            font-size: 52px;
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #6a11cb, #2575fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;">
            Affiliate Offers Dashboard
        </h1>
        <p style="
            font-size: 18px;
            font-weight: 400;
            color: #e0e0e0;
            margin-to
