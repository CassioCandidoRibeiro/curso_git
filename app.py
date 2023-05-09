# BIBLIOTECAS

import streamlit as st

from src.extration import load_data

# LAYOUT

st.set_page_config(layout='wide')

def main():
    df = load_data()
    st.dataframe(df)

