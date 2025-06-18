# utils/load_data.py

import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_excel(r"C:\Users\sarah\OneDrive\Documentos\GitHub\Final-Project\cleaned_version.xlsx")
    return df
